import pandas as pd
from collections import defaultdict
import csv


#csvFile = pd.read_csv(r'C:\Users\sofia\Documents\GitHub\experimento\Python\Ejercicio B\estrenos.csv')

#df= csvFile.applymap(str).groupby('fecha_estreno').apply(list).to_dict



with open("C:\Users\sofia\Documents\GitHub\experimento\Python\Ejercicio B\estrenos.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        print ('line[{}] = {}'.format(i, line))

