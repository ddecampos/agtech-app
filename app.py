from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# API Key de OpenWeatherMap
API_KEY = "WEATHER_API_KEY"

# Función para obtener los datos meteorológicos de la ubicación
def get_real_weather_data(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_data = {
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "description": data['weather'][0]['description'],
            "location": data['name'],
            "country": data['sys']['country']
        }
        return weather_data
    else:
        return {"error": "Unable to fetch weather data"}

# Ruta para obtener los datos reales del clima basado en latitud y longitud
@app.route('/real_weather', methods=['GET'])
def real_weather():
    lat = request.args.get('lat')  # Latitud pasada como parámetro
    lon = request.args.get('lon')  # Longitud pasada como parámetro

    if lat and lon:
        data = get_real_weather_data(lat, lon)
        return jsonify(data)
    else:
        return jsonify({"error": "Please provide lat and lon parameters"})

# Ruta principal
@app.route('/')
def index():
    return "AgTech Monitoring System - Para datos meteorológicos, pasa latitud y longitud en /real_weather"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
