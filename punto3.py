
libros = [
    {"titulo": "la metamorfosis", "autor": "frank kafka", "año de publicacion": "1890", "precio": "10000"},
    {"titulo": "El diario de Ana Frank", "autor": "Ana Frank", "año de publicacion": "1960", "precio": "30000"},
    {"titulo": "el psicoanalista", "autor": "autor desconocidp", "año de publicacion": "2000", "precio": "25000"}
]

def encontrar_libro_mas_costoso(libros):
    libro_mas_costoso = max(libros, key=lambda libro: libro["precio"])
    return libro_mas_costoso

libro_mas_costoso = encontrar_libro_mas_costoso(libros)

print("libro mas costoso")
print(f"titulo: {libro_mas_costoso}")
print(f"\cantidad de libros evaluados: {len(libros)}")

