import csv
from funciones import mostrardatos,mostrardatosanimales,Clase, Caracteristica
if __name__ == "__main__":
    print("Por favor dime como quieres mostrar el listado")
    print("1. Por clase")
    print("2. Por alguna caracteristicas")
    print("3. Agregar un nuevo animal")
    print("Por favor proporciona el numero de tu eleccion")
    Seleccion=input()
    #listazoo= mostrardatos()
infoclases=mostrardatos('Python/Ejercicio A/clases.csv')
datos_animales = mostrardatosanimales('Python/Ejercicio A/zoo.csv')
if int(Seleccion)==1:
    print("las clases existentes son:")
    infoclases=mostrardatos('Python/Ejercicio A/clases.csv')
    print("Ingrese el id de la clase")
    Id_clase=int(input())
    if Id_clase in infoclases:
            clase_tipo = infoclases.get(Id_clase)
            animales = (datos_animales, Id_clase)
            print(f"Animales de la clase '{clase_tipo}':")
            for animal in animales:
                print(f"Nombre: {animal['nombre_animal']}")
    else:
            print("Intenta con otro Id")

   
elif int(Seleccion)==2:
    print("Ingrese la caracteristica ")
    caracteristica = input()
    animales_caracterisiticas= Caracteristica(datos_animales, caracteristica)
    print(f"Resultados de la búsqueda '{caracteristica}':")
    for animal in animales_caracterisiticas:
         print(f"Nombre: {animal['nombre_animal']}")
else:
    print("Selecciona una opcion de las antes mencionadas")



