import streamlit as st
from controllers.data_controller import obtener_resumen_datos

st.set_page_config(page_title="Menú Principal", page_icon="📊", layout="wide")

# --- Encabezado ---
st.title("📊 Proyecto Final - Análisis de Ventas")
st.subheader("Equipo de Desarrollo")
st.write("""
**Integrantes:**
- Lucas Santamaría  
- Xavier González  
- Saúl Abrego
""")

# --- Mostrar datos ---
resumen, error = obtener_resumen_datos()

if error:
    st.warning(error)
else:
    st.success(f"✅ Datos cargados correctamente ({resumen['total_filas']} registros)")

    col1, col2 = st.columns(2)
    col1.metric("Total de registros", resumen["total_filas"])
    col2.metric("Productos únicos", resumen["productos_unicos"])

    st.dataframe(resumen["data"][:5])

# --- Navegación ---
st.write("---")
if st.button("Ver gráfica interactiva"):
    st.switch_page("pages/grafica.py")
