from flask import Flask, jsonify, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('Front-end/index.html')  # Serve index.html directly from static

@app.route('/get_weather')
def get_weather():
    city_name = request.args.get('cityName')
    if not city_name:
        return jsonify({"error": "No city provided"}), 400
    
    response = requests.get(f"http://goweather.herokuapp.com/weather/{city_name}")
    
    if response.status_code == 200:
        weather = json.loads(response.text)
        weather_data = {
            "description": weather.get("description", "No description available"),
            "temperature": weather.get("temperature", "N/A"),
            "wind": weather.get("wind", "N/A"),
            "forecast": weather.get("forecast", [])
        }
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Unable to fetch weather data"}), 500

if __name__ == "__main__":
    app.run(debug=True)
