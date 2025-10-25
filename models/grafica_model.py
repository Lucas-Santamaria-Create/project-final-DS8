from config.db import supabase

def get_sales_data():
    try:
        data = supabase.table("sales_data").select("*").execute()
        return data.data
    except Exception as e:
        print(f"Error obteniendo datos: {e}")
        return []
