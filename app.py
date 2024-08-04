from flask import Flask, request, render_template
import requests
import sqlite3

def create_database():
    conn = sqlite3.connect('cities.db')
    # Aquí puedes agregar más código para configurar la base de datos
    return conn

# Llamada a la función para crear la base de datos
conn = create_database()

app = Flask(__name__)

api_key = "aquí tu API key"
@app.route('/cities.txt')
def cities():
    return app.send_static_file('cities.txt')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ciudad = request.form['ciudad']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        # Aquí puedes procesar y mostrar los datos meteorológicos de la ciudad
        return render_template('resultados.html', data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()