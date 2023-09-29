import csv
from csv import DictWriter, DictReader
from datetime import datetime
import calendar

def guardar_datos(datos, hacia_archivo):
    campos = datos.keys()
    list_campos = list(campos)
    with open(hacia_archivo, 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=list_campos)
        dictwriter_object.writerow(datos)
        f_object.close()

def cargar_datos_mes(desde_archivo):
    datos = {}
    with open(desde_archivo, encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            fecha_estreno = fila['fecha_estreno']
            ew_string = fecha_estreno.replace(" ", "")
            date_obj = datetime.strptime(ew_string, '%Y-%m-%d')
            month = date_obj.month
            month_name = calendar.month_name[month]
            if month_name not in datos:
                datos[month_name] = []
            datos[month_name].append(fila)
    return datos

def cargar_datos_anio(desde_archivo):
    datos = {}
    with open(desde_archivo, encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            fecha_estreno = fila['fecha_estreno']
            ew_string = fecha_estreno.replace(" ", "")
            date_obj = datetime.strptime(ew_string, '%Y-%m-%d')
            year = date_obj.year
            if year not in datos:
                datos[year] = []
            datos[year].append(fila)
    return datos