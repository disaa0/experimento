import csv

first_filter = input("Selecciona el filtro a usar para listar los animales: \n1-> Clase\n2-> Caracteristica\n")

if first_filter == '1': # por clases
    with open(file=r"C:\Users\CSi PRO\Documents\GitHub\experimento\Python\Ejercicio A\clases.csv", mode="r", encoding="utf8") as text: #display de las distintas clases
        contenedor = csv.reader(text)
        for row in contenedor:
            print(f"{row[0]} | {row[1]}")

    desc = input("Introduce la clase de animales a buscar: ") #input de la clase a filtrar

    with open(file=r"C:\Users\CSi PRO\Documents\GitHub\experimento\Python\Ejercicio A\zoo.csv", mode="r", encoding="utf8") as text:
        contenedor = csv.reader(text)
        for row in contenedor:
            if row[17] == desc:
                print(row[0])

elif first_filter == '2': # por caracteristicas
    with open(file=r"C:\Users\CSi PRO\Documents\GitHub\experimento\Python\Ejercicio A\zoo.csv", mode="r", encoding="utf8") as text: #display de las distintas clases
        contenedor = text.readline()
        carac = contenedor.split(",")
        new_car = carac[1:16]
        for i in range(len(new_car)):
            print(f"{i+1} {new_car[i]}")
        desc = input("Introduce la caracteristica de los animales a buscar: ") #input de la clase a filtrar
        for row in contenedor:
            if row[17] == desc:
                print(row[0])
else:
    print("You did something wrong! :(")

            
