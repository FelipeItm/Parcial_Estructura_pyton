def Disponibilidad(r): #Declaracion de la funcion
    print("Estos son los productos que estan disponibles: \n")
    for obj in r: #Iteracion sobre cada uno de los objetos del diccionario para confirmar disponibilidad
        if obj["disponibilidad"] == 1:
            print(obj["nombre"])
            print(obj["descripcion"])
            print(obj["precio"])
            print("*" * 10)