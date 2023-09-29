import csv
#import pandas as pd

def leerCVS(archivo):
    with open(archivo, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def crear_diccionario_con_archivo_cvs(archivo):
    dict_from_csv = {}
    with open(archivo, mode='r') as inp:
        reader = csv.reader(inp)
        dict_from_csv = {rows[0]:rows[1] for rows in reader}

    print(dict_from_csv)

def crear_lista_diccionarios(archivo):
    lista = []
    with open(archivo) as csvfile:
        reader = csv.DictReader(csvfile)  
        
        for row in reader:
            lista.append(row) 

    return(lista) 



