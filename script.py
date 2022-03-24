from flask import Flask, render_template, request
import requests

app = Flask(__name__,template_folder='temps')

@app.route("/")
def weather_dashboard():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']

    api_key = '3d284bf0531bdddc51793cd4ff778cef'
    data = get_weather_results(zip_code, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    city = data["name"]
    country = data["sys"]["country"]

    return render_template('results.html',
                           city=city, country=country, temp=temp,
                           feels_like=feels_like, weather=weather)


def get_weather_results(zip_code, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    r = requests.get(api_url)
    return r.json()


if __name__ == '__main__':
    app.run(debug=True)


    


