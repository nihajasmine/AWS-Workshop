from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "529fa75a7728ee97042b7a7ed75ea332"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_weather", methods=["POST"])
def get_weather():
    city = request.json["city"]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()
    print(data)  # Debugging: Print the API response

    if data.get("cod") != 200:
        return jsonify({"error": "City not found. Check spelling or try another city."})

    weather_info = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }
    return jsonify(weather_info)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
