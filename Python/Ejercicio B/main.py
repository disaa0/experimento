
import funciones
import pandas as pd


def run():
    print("Bienvenido a la cartelera de estrenos")
    funciones.LeerArchivo('Python/Ejercicio B/estrenos.csv')
    funciones.imprimirCartelera()

    while True:
        print("1. Agregar pelicula")
        print("2. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == '1':
            funciones.agregarPelicula('Python/Ejercicio B/estrenos.csv')
        elif opcion == '2':
            break
if __name__ == '__main__':
    run()  