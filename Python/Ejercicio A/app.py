import csv
from funciones import lee_archivo_csv
if __name__ == "__main__":
    print("Por favor dime como quieres mostrar el listado")
    print("1. Por clase")
    print("2. Por alguna caracteristicas")
    print("3. Agregar un nuevo animal")
    print("Por favor proporciona el numero de tu eleccion")
    Seleccion=input()
    listaclases= lee_archivo_csv("Python/Ejercicio A/clases.csv")
    listazoo= lee_archivo_csv("Python/Ejercicio A/zoo.csv")
    for lista in listaclases:

        print(listaclases[lista])
    print(listazoo)
    
    
with open('Python/Ejercicio A/clases.csv') as file:
    csv_reader = csv.DictReader(file, delimiter=',')

    for row in csv_reader:
        claseid = row['Clase_id']
        clase_tipo = row['Clase_tipo']
        print('El id de la clase es:', claseid)
        print('El tipo de la clase es:',clase_tipo)

if int(Seleccion)==1:
    pass
elif int(Seleccion)==2:
    pass
else:
    print("Selecciona una opcion de las antes mencionadas")



