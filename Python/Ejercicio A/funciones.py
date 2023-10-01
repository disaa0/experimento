import csv


def crearDict(ruta: str):
    data = []
    with open(ruta) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append(row)
    return data


def relacionarClase(lista: list):
    clases = crearDict('clases.csv')

    for dic in lista:
        for key in dic:
            if key == 'clase':
                id_clase = dic[key]
                for elem in clases:
                    if elem['Clase_id'] == id_clase:
                        dic['clase'] = elem['Clase_tipo']
    return lista


def listar(columna=''):
    lista_zoo = crearDict('zoo.csv')
    if columna == '':
        relacionarClase(lista_zoo)
        return lista_zoo
    lista_filtrada = []
    for dic in lista_zoo:
        for key in dic:
            if key == 'clase' and dic[key] == columna:
                lista_filtrada.append(dic)
            if key == columna and dic[key] != '0':
                lista_filtrada.append(dic)
    relacionarClase(lista_filtrada)
    return lista_filtrada


def agregarAnimal(animal: dict):
    with open('zoo.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=animal.keys())
        # Append single row to CSV
        writer.writerow(animal)
