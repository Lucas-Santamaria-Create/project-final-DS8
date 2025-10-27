import os

import streamlit as st

from controllers.grafica_controller import obtener_resumen_datos


st.set_page_config(page_title="Menú Principal", page_icon="📊", layout="wide")

# --- Encabezado ---
st.markdown(
    """
<div class="title-box">
    <h1>📊 Proyecto Final - Análisis de Ventas</h1>
    <h3>Equipo de Desarrollo</h3>
    <p><b>Integrantes:</b><br>
    Lucas Santamaría<br>
    Xavier González<br>
    Saúl Abrego</p>
</div>
""",
    unsafe_allow_html=True,
)

# --- Datos ---
resumen, error = obtener_resumen_datos()

if error:
    st.warning(error)
else:
    st.success(f"✅ Datos cargados correctamente ({resumen['total_filas']} registros)")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric("📦 Total de registros", resumen["total_filas"])
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric("🛍️ Productos únicos", resumen["productos_unicos"])
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("### 🧮 Vista previa de los datos")
    st.dataframe(resumen["data"].head())

st.write("---")

