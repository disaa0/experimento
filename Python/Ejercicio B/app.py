from BasePeliculas import BasePeliculas
from Pelicula import Pelicula

def main():
    bd = BasePeliculas("C:\Users\CSI PRO\Documents\GitHub\experimento\Python\Ejercicio B\estrenos.csv")
    print("Quiere mostrar las peliculas ordendas alfabéticamente por título o título original?")
    print("1. Título")
    print("2. Título original")
    opcion = int(input("Ingrese una opción: "))
    if(opcion == 1):
        bd.diccionario["Enero"].registro[0].sort()
        bd.diccionario["Febrero"].registro[0].sort()
        bd.diccionario["Marzo"].registro[0].sort()
        bd.diccionario["Abril"].registro[0].sort()
        bd.diccionario["Mayo"].registro[0].sort()
        bd.diccionario["Junio"].registro[0].sort()
        bd.diccionario["Julio"].registro[0].sort()
        bd.diccionario["Agosto"].registro[0].sort()
        bd.diccionario["Septiembre"].registro[0].sort()
        bd.diccionario["Octubre"].registro[0].sort()
        bd.diccionario["Noviembre"].registro[0].sort()
        bd.diccionario["Diciembre"].registro[0].sort()

        for x in bd.diccionario["Enero"]:
            print("Enero\n__________________________")
            print(x)
        for x in bd.diccionario["Febrero"]:
            print("Febrero\n__________________________")
            print(x)
        for x in bd.diccionario["Marzo"]:
            print("Marzo\n__________________________")
            print(x)
        for x in bd.diccionario["Abril"]:
            print("Abril\n__________________________")
            print(x)
        for x in bd.diccionario["Mayo"]:
            print("Mayo\n__________________________")
            print(x)
        for x in bd.diccionario["Junio"]:
            print("Junio\n__________________________")
            print(x)
        for x in bd.diccionario["Julio"]:
            print("Julio\n__________________________")
            print(x)
        for x in bd.diccionario["Agosto"]:
            print("Agosto\n__________________________")
            print(x)
        for x in bd.diccionario["Septiembre"]:
            print("Septiembre\n__________________________")
            print(x)
        for x in bd.diccionario["Octubre"]:
            print("Octubre\n__________________________")
            print(x)
        for x in bd.diccionario["Noviembre"]:
            print("Noviembre\n__________________________")
            print(x)
        for x in bd.diccionario["Diciembre"]:
            print("Diciembre\n__________________________")
            print(x)
    if(opcion == 2):
        bd.diccionario["Enero"].registro[1].sort()
        bd.diccionario["Febrero"].registro[1].sort()
        bd.diccionario["Marzo"].registro[1].sort()
        bd.diccionario["Abril"].registro[1].sort()
        bd.diccionario["Mayo"].registro[1].sort()
        bd.diccionario["Junio"].registro[1].sort()
        bd.diccionario["Julio"].registro[1].sort()
        bd.diccionario["Agosto"].registro[1].sort()
        bd.diccionario["Septiembre"].registro[1].sort()
        bd.diccionario["Octubre"].registro[1].sort()
        bd.diccionario["Noviembre"].registro[1].sort()
        bd.diccionario["Diciembre"].registro[1].sort()

        for x in bd.diccionario["Enero"]:
            print("Enero\n__________________________")
            print(x)
        for x in bd.diccionario["Febrero"]:
            print("Febrero\n__________________________")
            print(x)
        for x in bd.diccionario["Marzo"]:
            print("Marzo\n__________________________")
            print(x)
        for x in bd.diccionario["Abril"]:
            print("Abril\n__________________________")
            print(x)
        for x in bd.diccionario["Mayo"]:
            print("Mayo\n__________________________")
            print(x)
        for x in bd.diccionario["Junio"]:
            print("Junio\n__________________________")
            print(x)
        for x in bd.diccionario["Julio"]:
            print("Julio\n__________________________")
            print(x)
        for x in bd.diccionario["Agosto"]:
            print("Agosto\n__________________________")
            print(x)
        for x in bd.diccionario["Septiembre"]:
            print("Septiembre\n__________________________")
            print(x)
        for x in bd.diccionario["Octubre"]:
            print("Octubre\n__________________________")
            print(x)
        for x in bd.diccionario["Noviembre"]:
            print("Noviembre\n__________________________")
            print(x)
        for x in bd.diccionario["Diciembre"]:
            print("Diciembre\n__________________________")
            print(x)

if __name__ == "__main__":
    bd = BasePeliculas("C:\Users\CSI PRO\Documents\GitHub\experimento\Python\Ejercicio B\estrenos.csv")
    print(bd.diccionario["Enero"][0].titulo)