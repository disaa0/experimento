## Instrucciones para el experimento
1. Llenar encuesta de entrada: https://forms.gle/FRD39iwwqL6d5p466
2. Abrir GitHub Desktop.
- ![1](https://github.com/disaa0/experimento/assets/85775871/b93db100-9452-4a27-8d18-68e3a0d226a2)
3. Hacer click en el apartado de ``Branch`` y seleccionar ``New Branch``
- ![2](https://github.com/disaa0/experimento/assets/85775871/584cd7cf-a55c-4667-85dd-db7b7c40eea8)
4. Escribir el nombre clave otorgado para cada participante. Este nombre es único y no debe contener espacios ni caracteres especiales.
5. Una vez creada la branch, hacer click en ``Open in Visual Studio Code``
- ![4](https://github.com/disaa0/experimento/assets/85775871/efa1a9c8-b064-4872-9e93-b54da76a3c50)
6. Crear archivo del programa en la carpeta que corresponda según el ejercicio a realizar.
- ![5](https://github.com/disaa0/experimento/assets/85775871/43cdcfdb-8710-4cf3-994a-06d969fdf178)
7. Escribir el código del programa en el campo de edición de texto, las instrucciones para cada programa se encuentran al final.
8. Guardar el archivo.
9. Volver a GitHub Desktop y hacer un Commit en la branch creada anteriormente. 
- ![6](https://github.com/disaa0/experimento/assets/85775871/cb07f0b7-1f9e-40a8-93fd-8bde3f1307cd)
10. Hacer clic en el botón ``Publish Branch`` para subir los cambios a la branch creada.
- ![7](https://github.com/disaa0/experimento/assets/85775871/845b7165-3292-4a94-a26e-d1bd3f7f0541)
11. Llenar encuesta de salida según grupo:
- Para Grupo "Sin Asistencia": https://forms.gle/wdQKLvap6EkTKAeh7
- Para Grupo "Con asistencia": https://forms.gle/qaarHxpdR2e86g5o8


¡Listo!
# Problematicas de Python
## Ejercicio A

Realizar un programa en Python que permita listar animales por dos condiciones:

- Por su clasificación o clase
- Por alguna de sus características

El programa deberá contar con un menú que permita seleccionar el listado por clase o listar por alguna característica.
Si tiene tiempo, debe escribir un módulo que permita agregar un nuevo animal o varios animales  al listado. Al salir, se deberán grabar los cambios realizados, para que al volver a entrar al programa, no sea necesario volver a agregarlos.

Es recomendable que se divida el programa en dos archivos: Un archivo de funciones auxiliares donde se encuentren las funciones que hacen todo el procesamiento y otro donde se encuentre la ejecución de la lógica principal, llamando a las funciones. 
Hay dos archivos csv: clases.csv y zoo.csv, es necesario escribir una sola función que cargue el contenido de un archivo en un diccionario. Así la función podrá ser usada para cargar un archivo a la vez en el diccionario de clases y en el diccionario de animales.

Puede realizar el programa con interface para consola de texto o de página dinámica web (Flask o Django)

## Ejercicio B

Desarrollar un programa en Python, bajo el paradigma de Objetos. La funcionalidad del programa es la siguiente:

Leer el archivo estrenos.csv, generar los objetos del tipo Película y agregarlos a un diccionario, donde la llave es el mes de estreno de la película, y el valor es una lista de películas que se estrenan en ese mes. Después, ciclar ese diccionario, para desplegar mes por mes, las películas que se estrenan.

El programa deberá contar con un menú que permita seleccionar el listado por clase o listar por alguna característica.
Si tiene tiempo, debe escribir un módulo que permita agregar una o varias nuevas películas  al listado. Al salir, se deberán grabar los cambios realizados, para que al volver a entrar al programa, no sea necesario volver a agregarlos.

Es recomendable que se divida el programa en dos archivos: Un archivo de funciones auxiliares donde se encuentren las funciones que hacen todo el procesamiento y otro donde se encuentre la ejecución de la lógica principal, llamando a las funciones.

Puede realizar el programa con interface para consola de texto o de página dinámica web (Flask o Django)

# Problematicas de JavaScript
## Ejercicio A
Escribir una aplicación en JavaScript para evaluar una expresión aritmética. Las operaciones que puede incluir la expresión son: suma (+), resta (-), multiplicación (*) y división (/). Cuando la expresión aritmética involucra sumas, restas, multiplicaciones y/o divisiones el orden en el que se deben realizar las operaciones es:

- Operaciones agrupadas en paréntesis.
- Multiplicaciones y divisiones
- Sumas y restas


Si la expresión contiene algún error, la aplicación debe notificar al usuario.
