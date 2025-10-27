import os

import streamlit as st

from controllers.grafica_controller import obtener_resumen_datos


# --- Función para cargar CSS ---
def load_css(file_name):
    css_path = os.path.join(os.path.dirname(__file__), file_name)
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"No se encontró el archivo CSS: {file_name}")


# --- Cargar CSS antes que cualquier st.markdown o st.dataframe ---
load_css("styles/principal.css")

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
st.markdown(
    """
    <div style="text-align:center;">
        <a href="/pages/grafica" target="_self">
            <button class="custom-button">📈 Ver gráfica interactiva</button>
        </a>
    </div>
""",
    unsafe_allow_html=True,
)
