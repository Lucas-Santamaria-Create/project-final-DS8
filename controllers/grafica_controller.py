import pandas as pd

from models.obtener_datos import get_sales_data


def obtener_resumen_datos():
    try:
        # Obtienes los datos desde el modelo (lista de dicts)
        data = get_sales_data()  # Devuelve lista de diccionarios

        # Convertimos a DataFrame **aquí**, en el controlador
        df = pd.DataFrame(data)

        resumen = {
            "data": df,
            "total_filas": len(df),
            "productos_unicos": df["product"].nunique(),
        }

        return resumen, None

    except Exception as e:
        return None, str(e)
