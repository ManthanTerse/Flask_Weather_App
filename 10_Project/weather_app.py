#Project 10 : Flask Weather App 

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '947c3c7fae6cee82c0c66aaeb503a5ca'  

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None

    if request.method == 'POST':
        city = request.form['city']
        if city:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather = {
                    'city': city.title(),
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                error = "City not found or API issue."

    return render_template('index.html', weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True)
