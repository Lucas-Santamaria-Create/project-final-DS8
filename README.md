# Proyecto Final - Análisis de Ventas con IoT

Una aplicación web interactiva para el análisis de datos de ventas, construida con Streamlit. Incluye integración con Raspberry Pi para control IoT, alojada en Railway para comunicación remota y gestión de datos en tiempo real.

## 📋 Descripción

Este proyecto combina análisis de datos con control IoT para proporcionar una plataforma completa de visualización y gestión de ventas. La aplicación permite cargar datos de ventas, mostrar métricas clave y generar gráficos interactivos, todo mientras se comunica con dispositivos IoT conectados a una Raspberry Pi.

## ✨ Características

- **Análisis de Ventas**: Visualización de métricas clave como total de registros y productos únicos.
- **Gráficos Interactivos**: Página dedicada para explorar datos a través de gráficos dinámicos.
- **Integración IoT**: Comunicación con Raspberry Pi para envío y recepción de datos e instrucciones.
- **Interfaz Web**: Aplicación web responsiva construida con Streamlit.
- **Alojamiento Remoto**: Desplegada en Railway para acceso remoto.

## 🛠️ Tecnologías Utilizadas

- **Streamlit** – Framework principal
- **Python 3.11+**
- **Pandas** – Análisis de datos
- **Plotly Express** – Visualización interactiva
- **Supabase** – Base de datos en la nube
- **Raspberry Pi + GPIO/MQTT** – Dispositivo IoT
- **Railway** – Despliegue en la nube
- **GitHub Actions** – CI/CD y linting con Ruff

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/project-final-DS8.git
   cd project-final-DS8
   ```

2. Crear entorno virtual
    ```
    python -m venv venv
    source venv/bin/activate   # En Linux/Mac
    venv\Scripts\activate      # En Windows
    ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## 📖 Uso

- Accede a la aplicación en tu navegador.
- Revisa las métricas de ventas en la página principal.
- Haz clic en "Ver gráfica interactiva" para explorar los datos visualmente.
- La integración IoT permite comunicación remota con la Raspberry Pi.

## 👥 Equipo de Desarrollo

- **Lucas Santamaría**
- **Xavier González**
- **Saúl Abrego**

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
