from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "940365387a2b3f66a145274427fd44c7"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_weather", methods=["POST"])
def get_weather():
    city = request.form["city"]

    if not city or not not_validate_name(city):
        return render_template("index.html", error="Please enter a valid city name.")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],

            "description": data["weather"][0]["description"],

            "temperature": data["main"]["temp"],

            "humidity": data["main"]["humidity"],

            "wind_speed": data["wind"]["speed"],

            "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"

        }
        return render_template("index.html", weather=weather)
    elif response.status_code == 404:
        return render_template("index.html", error="City not found. Please enter a valid city name.")
    else:
        return render_template("index.html", error="An error occurred while fetching the weather data. Please try again later.")

def not_validate_name(city):
    return all(part.isalpha() for part in city.split()) and len(city) > 1

if __name__ == "__main__":
    app.run(debug=True)