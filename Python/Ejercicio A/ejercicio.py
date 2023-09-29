#Realizar un programa en Python que permita listar animales por dos 
#condiciones:

#Por su clasificación o clase
#Por alguna de sus características
#El programa deberá contar con un menú que permita 
#el listado por clase o listar por alguna característica. 
#Si tiene tiempo, debe escribir un módulo que permita agregar un 
#nuevo animal o varios animales al listado. Al salir, se deberán 
#grabar los cambios realizados, para que al volver a entrar al 
#programa, no sea necesario volver a agregarlos.

#Es recomendable que se divida el programa en dos archivos:
#Un archivo de funciones auxiliares donde se encuentren las 
#funciones que hacen todo el procesamiento y otro donde se 
#encuentre la ejecución de la lógica principal, llamando a las 
#funciones. Hay dos archivos csv: clases.csv y zoo.csv, es necesario 
#escribir una sola función que cargue el contenido de un archivo en 
#un diccionario. Así la función podrá ser usada para cargar un 
#archivo a la vez en el diccionario de clases y en el diccionario 
#de animales.

#Puede realizar el programa con interface para consola de texto o 
#de página dinámica web (Flask o Django)
import funciones
from funciones import *

#print(leerCVS(r"\Users\karla\OneDrive\Documents\GitHub\experimento\Python\Ejercicio A\clases.csv"))

#diccionario = leerCVS(r"\Users\karla\OneDrive\Documents\GitHub\experimento\Python\Ejercicio A\clases.csv")
#crear_diccionario_con_archivo_cvs(r"\Users\karla\OneDrive\Documents\GitHub\experimento\Python\Ejercicio A\clases.csv")





lista_clases = crear_lista_diccionarios(r"\Users\karla\OneDrive\Documents\GitHub\experimento\Python\Ejercicio A\clases.csv")
lista_zoo = crear_lista_diccionarios(r"\Users\karla\OneDrive\Documents\GitHub\experimento\Python\Ejercicio A\zoo.csv")
#print(lista_zoo)

print("Seleccione un numero dependiendo de lo que desee: ")
print("Listar por clases los animales del zoologico: ------------>0")
print("Listar por características los animales del zoologico: --->1")
respuesta = input()

if respuesta == "1":
    print("USTED SELECCIONO LISTADO POR CLASES")
    print("----------------------------------")
    print("lISTADO DE ANIMALES POR CLASES: ")

    for elem in lista_zoo:      #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        nombre = ''
        clase=''
        clase_nombre=''
        #print(elem) 
        for a,b in elem.items():
            if a=="nombre_animal":
                nombre = b
                print("este es el nombre: ", nombre)
            if a=="clase":
                clase = b
                print("esta es la clase: ",clase)

                for elem in lista_clases:
                    for c,d in elem.items():
                        if clase == d:
                            clase_nombre = d[0]
                            print("esta es el nombre de la clase: ",clase_nombre)
        

        print("-----------")
#
        #    nombre = "";
        #    clase = "";
        #    if a == "nombre_animal":
        #        nombre == b
        #    if a == "clase":
        #        clase = b;
            
        #print("El nombre del animal es ",nombre, "y su clase: ", b )
            #print("ESTE ES A: ",a)
            #print("ESTE ES B: ",b)
            #for elem in lista_clases:
            #    for c,d in elem.items():
                     
                    


            
elif respuesta == "0":
    print("USTED SELECCIONO LISTADO POR CLASES")
else:
    print("USTRED SELECCIONÓ UNA OPCIÓN NO VALIDA")