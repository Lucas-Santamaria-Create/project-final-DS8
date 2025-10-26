import os
from supabase import create_client
import streamlit as st

@st.cache_resource
def init_connection():
    # Intentar obtener de variables de entorno primero
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")

    # Si no están en entorno, intentar de secrets de Streamlit
    if not url or not key:
        try:
            url = st.secrets["SUPABASE_URL"]
            key = st.secrets["SUPABASE_KEY"]
        except KeyError:
            st.error("Faltan las variables de entorno SUPABASE_URL o SUPABASE_KEY, y no se encontraron en secrets.toml")
            return None

    if not url or not key:
        st.error("Faltan las variables de entorno SUPABASE_URL o SUPABASE_KEY")
        return None
    return create_client(url, key)

supabase = init_connection()
