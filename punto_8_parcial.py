# Shara García Betancur - Punto 8 - Parcial 1
# La empresa yupi tiene 5 vendedores los cuales están compitiendo por el empleado del año,
# para tener en cuenta el premio, se debe agrupar las ventas por vendedor,
# el problema que requieren solucionar es sumar las ventas por cada vendedor,
# para poder identificar cuál de todos vendió mas por el año, para poder mostrar el nombre,
# teléfono, venta del ganador. Se debe tener en cuenta que las ventas están representadas por mes.

class Vendedor:
    def __init__(self, nombre, telefono, ventas):
        self.nombre = nombre
        self.telefono = telefono
        self.ventas = ventas
        
    def __repr__(self):
        return f'Vendedor("{self.nombre}", {self.telefono}, {self.ventas})'


# Función para sumar las ventas por vendedor e identificar al mejor vendedor
def sum_ventas_vendedor(matriz, vendedores):
    max_ventas = 0
    mejor_vendedor = None
    
    for vendedor, fila in enumerate(matriz):
        suma_ventas = sum(fila)
        vendedores[vendedor].ventas = fila
        if suma_ventas > max_ventas:
            max_ventas = suma_ventas
            mejor_vendedor = vendedores[vendedor]
            
    return mejor_vendedor, max_ventas


# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for vendedor in matriz:
        print(vendedor)


def main():
    # Crear la matriz de vendedores
    vendedores = [
        Vendedor("Camilo", 3015896312, []),
        Vendedor("Shara", 3234893508, []),
        Vendedor("Robinson", 3004691662, []),
        Vendedor("Valentina", 3124562516, []),
        Vendedor("Michael", 3009693278, [])
    ]
    
    # Crear la matriz de ventas (5 filas, 12 columnas)
    matriz_ventas = [
        [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550, 700],
        [500, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100],
        [200, 300, 250, 400, 350, 500, 450, 600, 550, 700, 650, 800],
        [400, 500, 450, 600, 550, 700, 650, 800, 750, 900, 850, 1000],
        [300, 400, 350, 500, 450, 600, 550, 700, 650, 800, 750, 900],
    ]

    # Identificar al mejor vendedor
    mejor_vendedor, ventas = sum_ventas_vendedor(matriz_ventas, vendedores)
    
    print("Matriz de ventas:")
    imprimir_matriz(vendedores)
    
    print(f"\nEl/La mejor vendedor/a es {mejor_vendedor.nombre}, con número de télefono {mejor_vendedor.telefono} con ventas totales de {ventas}")


if __name__ == "__main__":
    main()
