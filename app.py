# app.py

def calcular_precio_con_descuento(precio_base, porcentaje_descuento):
    """
    Calcula el precio final aplicando un descuento.
    """
    if precio_base < 0 or porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("Precio o porcentaje no válidos.")
        
    # **BUG INTENCIONAL:** Se resta el porcentaje directamente, no el porcentaje del precio.
    # Precio final esperado para 100 con 10%: 90
    # Precio final CREADO con el bug: 100 * (1 - 10) = -900 (¡Esto causará el error!)
    #precio_final = precio_base * (1 - porcentaje_descuento)
    precio_final = precio_base * (1 - porcentaje_descuento / 100)
    return round(precio_final, 2)