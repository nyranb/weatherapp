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
    current_data = get_current_weather(zip_code, api_key)
    daily_data = get_daily_weather(zip_code, api_key)
    temp = "{0:.2f}".format(current_data["main"]["temp"])
    feels_like = "{0:.2f}".format(current_data["main"]["feels_like"])
    weather = current_data["weather"][0]["main"]
    city = current_data["name"]
    country = current_data["sys"]["country"]
    icon = "https://openweathermap.org/img/wn/" + current_data["weather"][0]["icon"] + "@2x.png"

    return render_template('results.html',
                           city=city, country=country, temp=temp,
                           feels_like=feels_like, weather=weather, icon=icon)


def get_current_weather(zip_code, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    r = requests.get(api_url)
    return r.json()

def get_daily_weather(zip_code, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/forecast/daily?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    r = requests.get(api_url)
    return r.json()



if __name__ == '__main__':
    app.run(debug=True)


    


