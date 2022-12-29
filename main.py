from flask import Flask, request, render_template
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():

    weatherData = ''
    metric = "metric"
    error = 0
    cityName = ''
    if request.method == "POST":
        cityName = request.form.get("cityName")
        if cityName:
            weatherApiKey = 'Your API Key'
            url = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&units="+metric+ "&appid=" + weatherApiKey
            weatherData = requests.get(url).json()
        else:
            error = 1
    return render_template('index.html', data=weatherData, cityName=cityName, error=error,current_year=datetime.now().year)


if __name__ == "__main__":
    app.run()