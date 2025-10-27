import os


from supabase import create_client


import streamlit as st





@st.cache_resource


def init_connection():


    url = os.environ.get("SUPABASE_URL")


    key = os.environ.get("SUPABASE_KEY")


    if not url or not key:


        st.error("Faltan las variables de entorno SUPABASE_URL o SUPABASE_KEY")


        return None


    return create_client(url, key)





supabase = init_connection()