import csv
import pandas

with open('estrenos.csv', 'r', encoding='utf-8') as estrenos:
    lector = csv.reader(estrenos)
    encabezados = next(lector)

    informacion = []
    for fila in lector:
        record = {}
        mes = int(fila[3].split('-')[1])
        for i, value in enumerate(fila):
            record[encabezados[i]] = value
        informacion.append(record)


df = pandas.DataFrame(informacion)
df = df.drop(columns=['url_imagen'])

print('Seleccionador de estrenos por mes')
print('Seleccione un mes')
print('1. Enero')
print('2. Febrero')
print('3. Marzo')
print('4. Abril')
print('5. Mayo')
print('6. Junio')
print('7. Julio')
print('8. Agosto')
print('9. Septiembre')
print('10. Octubre')
print('11. Noviembre')
print('12. Diciembre')

mes = int(input('Ingrese un mes: '))
df_mes = df[df['fecha_estreno'].str.contains(f'-{mes:02d}-')]
if df_mes.empty:
    print('No hay estrenos en este mes')
else:
    print(df_mes)
