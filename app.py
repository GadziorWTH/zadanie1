import os
from flask import Flask, request, jsonify
from datetime import datetime
import requests

app = Flask(__name__)
port = int(os.environ.get("PORT", 8080))
author = "Michal Mironczuk"

@app.route("/")
def index():
    return """
    <form action="/weather" method="post">
        Country: <input type="text" name"country"><br>
        City: <input type="text" name="city"><br>
        <input type="submit" value"Get Weather">
    </form>
    """

@app.route("/weather", methods=["POST"])
def get_weather():
    country = request.form["country"]
    city = request.form["city"]
    api_key = os.environ.get("API_KEY")

    if not api_key:
        return "Brak klucza API", 500

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Błąd: {response.json().get('message', 'Nieznany błąd')}", 400

    data = response.json()
    temp = data["main"]["temp"]
    return f"Pogoda w {city}, {country}: {temp}°C"

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    print(f"Data uruchomienia: {datetime.now()}")
    print(f"Autor: {author}")
    print(f"Port TCP: {port}")
    app.run(host="0.0.0.0", port=port)