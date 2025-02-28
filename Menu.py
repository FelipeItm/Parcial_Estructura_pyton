from Punto5 import Disponibilidad

Repuestos = [{"nombre":"Tornillo", "descripcion":"4 milimetros" ,"precio":200, "disponibilidad":1},
             {"nombre":"Llanta", "descripcion":"Trasera", "precio":22000, "disponibilidad":0},
             {"nombre":"Luces Led", "descripcion":"Luces Farola adelante", "precio":125000, "disponibilidad":1},
             {"nombre":"Bujia", "descripcion":"Encendio" ,"precio":200, "disponibilidad":1},
             {"nombre":"Tapa", "descripcion":"Lateral", "precio":33000, "disponibilidad":0},
             {"nombre":"Farola", "descripcion":"Trasera","precio":2500, "disponibilidad":0},
             {"nombre":"Valinera", "descripcion":"Delantera","precio":46000, "disponibilidad":1},
             {"nombre":"Cunas", "descripcion":"Delanteras","precio":15000, "disponibilidad":1},
             {"nombre":"Stickers", "descripcion":"Mofle","precio":150, "disponibilidad":0},
             {"nombre":"Eje", "descripcion":"Delantero", "precio":38000, "disponibilidad":1}
             ]

opc = None
opc = int(input("Digite una opcion: "))


if opc == 1:
    pass
elif opc == 2:
    pass   
elif opc == 3:
    pass
elif opc == 4:
    pass   
elif opc == 5:
    print(Disponibilidad(Repuestos))
elif opc == 6:
    pass   
elif opc == 7:
    pass
elif opc == 8:
    pass   
else:
    print("Respuesta equivocada")