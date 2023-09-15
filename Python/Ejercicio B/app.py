from flask import Flask, render_template, request
from funciones import lee_diccionario_estrenos
app = Flask(__name__)  

diccionario_estrenos = lee_diccionario_estrenos("estrenos.csv")
#print(diccionario_estrenos)
@app.route('/')
def index():
    return render_template('index.html', peliculas=diccionario_estrenos)

if __name__ == '__main__':
    app.run(debug=True)