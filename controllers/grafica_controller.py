from models.sales_model import get_sales_data


def obtener_resumen_datos():
    """Devuelve un resumen de los datos para mostrar en la vista."""
    data = get_sales_data()
    if not data:
        return None, "No hay datos en la tabla."

    total_filas = len(data)
    productos_unicos = len(set([item["product"] for item in data]))
    return {
        "total_filas": total_filas,
        "productos_unicos": productos_unicos,
        "data": data,
    }, None
