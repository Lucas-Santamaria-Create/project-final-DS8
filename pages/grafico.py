# pages/grafico.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from config.db import supabase  # Importa correctamente desde config/
import streamlit as st
import pandas as pd
import plotly.express as px


# Detener la app si la conexión no está disponible
if not supabase:
    st.error("No se pudo conectar a la base de datos.")
    st.stop()

# Título de la página
st.title("📊 Visualización de Datos")

# Nombre de la tabla en Supabase
table_name = "sales_data"  # Cambia esto por tu tabla real

try:
    # Consultar todos los registros de la tabla
    response = supabase.table(table_name).select("*").execute()
    
    # Convertir a DataFrame, asegurando que no falle si no hay datos
    data = pd.DataFrame(response.data if hasattr(response, "data") else [])

    if not data.empty:
        st.success(f"Datos cargados correctamente ({len(data)} registros).")

        # Vista previa de la tabla
        st.subheader("Vista previa de la tabla")
        st.dataframe(data.head())

        # Selección de columnas para la gráfica
        st.subheader("Selecciona columnas para la gráfica")
        x_axis = st.selectbox("Eje X:", data.columns)
        y_axis = st.selectbox("Eje Y:", data.columns)

        # Crear gráfica interactiva con Plotly
        fig = px.line(data, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
        st.plotly_chart(fig, use_container_width=True)

        # Estadísticas básicas
        st.subheader("📈 Estadísticas")
        st.write(data.describe())

        # Botón para volver al menú principal (si aplica)
        if st.button("⬅️ Volver al menú principal"):
            st.experimental_rerun()

    else:
        st.warning("No hay datos en la tabla.")

except Exception as e:
    st.error(f"Error al obtener datos: {e}")
