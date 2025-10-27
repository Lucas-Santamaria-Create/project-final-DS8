from config.db import supabase


def get_sales_data():
    """Obtiene todos los datos de ventas desde Supabase."""
    try:
        response = supabase.table("sales_data").select("*").execute()
        return response.data
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return []
