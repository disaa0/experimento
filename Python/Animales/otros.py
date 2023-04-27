import csv

def cargar_archivo(nombre_archivo):
    # https://www.geeksforgeeks.org/reading-csv-files-in-python/
    # opening the CSV file
    lista_diccionarios = []
    with open(nombre_archivo, mode ='r', encoding="utf-8")as file:
        # reading the CSV file
        csvFile = csv.DictReader(file)
        for row in csvFile:
            lista_diccionarios.append(dict(row))
    return lista_diccionarios



def relacionar_diccionarios(list_1, list_2):
    lista_diccionario_relacionado = list_1.copy()
    for i in range(0, len(list_1)):
        animal = list_1[i]
        for clase in list_2:
            id_clase = clase["Clase_id"]
            if id_clase == animal["clase"]:
                nombre_clase = clase["Clase_tipo"]
                lista_diccionario_relacionado[i]["Clase_tipo"] = nombre_clase
                break
    print(lista_diccionario_relacionado)
    return lista_diccionario_relacionado