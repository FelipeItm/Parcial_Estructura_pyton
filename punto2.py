
ventas = [
    {"mes": "Enero", "ventas": 1000.0},
    {"mes": "Febrero", "ventas": 1200.0},
    {"mes": "Marzo", "ventas": 1500.0},
    {"mes": "Abril", "ventas": 1800.0},
    {"mes": "Mayo", "ventas": 2000.0},]

def encontrar_ventas_abril(ventas):
    ventas_abril = [venta for venta in ventas if venta["mes"] == "Abril"]
    if ventas_abril:
        return ventas_abril[0]["ventas"]
    else:
        return 0.0
    
ventas_abril = encontrar_ventas_abril(ventas)

print(f"Ventas totales de abril: ${ventas_abril:.2f}")