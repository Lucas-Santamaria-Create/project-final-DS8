import os
import streamlit as st

# --- Tu app aquí ---
st.title("🚀 App Streamlit corriendo en Railway")
st.write("Comunicación con Raspberry Pi")

# --- Configurar el puerto dinámico (muy importante) ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8501))
    os.system(f"streamlit run app.py --server.port {port} --server.address 0.0.0.0")
