import ejercicios

contenedor = ejercicios.csv_to_dict("C:\Users\CSi PRO\Documents\GitHub\experimento\Python\Ejercicio A\clases.csv")
for row in contenedor:
    print(f"{row[0]} | {row[1]}")