pass: Ur6LDHjEvvW6bn
## Enlaces a encuestas
Encuesta de entrada - Global: https://forms.gle/LaarYDVf9imn4pgN7

Encuesta de salida - Sin asistencia: https://forms.gle/UTdMyyBmCSRMPsR86

## Instrucciones para el experimento
Estas son las instrucciones para crear una branch individual y subir los ejercicios desde Visual Studio Code, con un nombre clave otorgado a cada participante del experimento.
1. Seleccionar la opción "Create Branch" en la pestaña "Source Control".
- ![2023-04-19_00-19](https://user-images.githubusercontent.com/85775871/232935046-99014cf4-d8b2-46dd-8881-9af643c46580.png)
2. Escribir el nombre clave otorgado para cada participante. Este nombre debe ser único para cada uno, y no debe contener espacios ni caracteres especiales.
3. Seleccionar la nueva branch creada en la lista desplegable de branches.
- ![2023-04-19_00-19_1](https://user-images.githubusercontent.com/85775871/232935187-70cfa2d6-93c2-46c4-a05b-f1cc31581e86.png)
4. Crear una carpeta en el directorio local del repositorio con el nombre del ejercicio a realizar.
5. Abrir Visual Studio Code en la carpeta recién creada y crear un nuevo archivo con el nombre del ejercicio y extensión ".py" para el ejercicio en Python, o ".js" para el ejercicio en JavaScript.
- ![2023-04-19_00-29](https://user-images.githubusercontent.com/85775871/232935666-b6cb7ee2-a634-4276-8f98-0c2449979fba.png)
6. Escribir el código del programa en el campo de edición de texto.
7. Guardar el archivo.
8. Volver a la pestaña "Source Control" y hacer clic en el botón "+" para agregar los cambios al área de staging.
- ![2023-04-19_00-21](https://user-images.githubusercontent.com/85775871/232935699-baf14f65-50bf-4e3e-8b72-a94dc770a1dc.png)
9. Escribir un mensaje de commit breve y descriptivo en el campo de texto "Message" y hacer clic en el botón de checkmark para confirmar el commit.
- ![2023-04-19_00-22](https://user-images.githubusercontent.com/85775871/232939140-6d068537-94bd-4a05-bccb-f2bcda0b6673.png)
10. Hacer clic en el botón "Push"/"Publish Branch" para subir los cambios a la branch creada.
- ![2023-04-19_00-22_1](https://user-images.githubusercontent.com/85775871/232935732-dd7876f9-9d04-4a2e-909f-ffbb489f0dc2.png)

¡Listo!

# Problemtica de Python #1

Realizar un programa en Python que permita listar animales por dos condiciones:
    a) Por su clasificación o clase
    b) Por alguna de sus características
El programa deberá contar con un menú que permita seleccionar el listado por clase o listar por alguna característica.
Si tiene tiempo, debe escribir un módulo que permita agregar un nuevo animal o varios animales  al listado. Al salir, se deberán grabar los cambios realizados, para que al volver a entrar al programa, no sea necesario volver a agregarlos.

Es recomendable que se divida el programa en dos archivos: Un archivo de funciones auxiliares donde se encuentren las funciones que hacen todo el procesamiento y otro donde se encuentre la ejecución de la lógica principal, llamando a las funciones. 
Hay dos archivos csv: clases.csv y zoo.csv, es necesario escribir una sola función que cargue el contenido de un archivo en un diccionario. Así la función podrá ser usada para cargar un archivo a la vez en el diccionario de clases y en el diccionario de animales.

Puede realizar el programa con interface para consola de texto o de página dinámica web (Flask o Django)

# Problematica de Python #2

Desarrollar un programa en Python, bajo el paradigma de Objetos. La funcionalidad del programa es la siguiente:

Leer el archivo estrenos.csv, generar los objetos del tipo Película y agregarlos a un diccionario, donde la llave es el mes de estreno de la película, y el valor es una lista de películas que se estrenan en ese mes. Después, ciclar ese diccionario, para desplegar mes por mes, las películas que se estrenan.

El programa deberá contar con un menú que permita seleccionar el listado por clase o listar por alguna característica.
Si tiene tiempo, debe escribir un módulo que permita agregar una o varias nuevas películas  al listado. Al salir, se deberán grabar los cambios realizados, para que al volver a entrar al programa, no sea necesario volver a agregarlos.

Es recomendable que se divida el programa en dos archivos: Un archivo de funciones auxiliares donde se encuentren las funciones que hacen todo el procesamiento y otro donde se encuentre la ejecución de la lógica principal, llamando a las funciones.

Puede realizar el programa con interface para consola de texto o de página dinámica web (Flask o Django)
