import streamlit as st
import os
from supabase import create_client

@st.cache_resource
def init_connection():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        st.error("Faltan las variables de entorno SUPABASE_URL o SUPABASE_KEY")
    return create_client(url, key)

supabase = init_connection()

st.title("Mi App Streamlit + Supabase")

# --- Formulario para agregar datos ---
st.header("Agregar un nuevo registro")
with st.form("add_form"):
    name = st.text_input("Nombre")
    pet = st.text_input("Mascota")
    submitted = st.form_submit_button("Agregar")

    if submitted:
        if name and pet:
            try:
                supabase.table("mytable").insert({"name": name, "pet": pet}).execute()
                st.success(f"Registro agregado: {name} - {pet}")
            except Exception as e:
                st.error(f"No se pudo agregar el registro: {e}")
        else:
            st.warning("Debes ingresar ambos campos")

# --- Mostrar datos existentes ---
st.header("Datos de mytable")
try:
    rows = supabase.table("mytable").select("*").execute()
    if rows.data:
        st.dataframe(rows.data)
    else:
        st.info("No hay datos en la tabla")
except Exception as e:
    st.error(f"No se pudieron obtener los datos: {e}")
