import csv

archivo_estrenos = 'estrenos.csv'
lista = []
diccionario = {}

with open (archivo_estrenos, 'r', encoding='utf-8') as fh:
    csv_reader = csv.DictReader(fh)
    for renglon in csv_reader:
        #print(renglon)
        texto_limpio = renglon['fecha_estreno'].strip()
        #print(texto_limpio)
        mes_1= texto_limpio[5:]
        mes_final = mes_1[:2]
        print(mes_final)
        if mes_final not in lista:
            lista.append(mes_final)
        
        #Create a dictionary with the month as key and the movies as values as a list to include multiple movies
        if mes_final not in diccionario:
            diccionario[mes_final] = [renglon]
        else:
            diccionario[mes_final].append(renglon)
    
        

        #diccionario[mes_final] = renglon


#print(lista)
#print(diccionario.get('04'))
#Return the dictionary to be used in Ejercicio.py
def diccionario():
    return diccionario