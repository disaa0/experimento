
#Import diccionario from Funciones.py
from Funciones import diccionario

#Create a terminal interface to interact with the user to ask for the key and display the movies
print('Bienvenido a la cartelera de estrenos')
print('-------------------------------------')
print('De que manera quieres buscar la pelicula?')
print('1. Por mes de estreno')
print('2. Por titulo')
print('3. Titulo Original')

input_usuario = input('Ingresa tu opcion: ')
if input_usuario == '1':
    mes = input('Ingresa el mes de estreno (mm): ')
    print(f'Estos son los estrenos del mes {mes}')
    print('-------------------------------------')
    for pelicula in diccionario.get(mes):
        print(pelicula['titulo'])
"""
elif input_usuario == '2':
    titulo = input('Ingresa el titulo de la pelicula: ')
    print(f'Estos son los estrenos con el titulo {titulo}')
    print('-------------------------------------')
    for pelicula in diccionario.get(titulo):
        print(pelicula['titulo'])
elif input_usuario == '3':
    titulo_original = input('Ingresa el titulo original de la pelicula: ')
    print(f'Estos son los estrenos con el titulo original {titulo_original}')
    print('-------------------------------------')
    for pelicula in diccionario.get(titulo_original):
        print(pelicula['titulo'])
else:
    print('Opcion no valida')
"""