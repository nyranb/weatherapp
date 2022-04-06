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
    
    for count, day in enumerate(daily_data['list']):
        globals()[f'temp{count}'] = day['temp']['day']
        globals()[f'icon{count}'] = "https://openweathermap.org/img/wn/" + day['weather'][0]['icon'] + "@2x.png"
        globals()[f'weather{count}'] = day['weather'][0]['main']


    temp = "{0:.2f}".format(current_data["main"]["temp"])
    feels_like = "{0:.2f}".format(current_data["main"]["feels_like"])
    weather = current_data["weather"][0]["main"]
    city = current_data["name"]
    country = current_data["sys"]["country"]
    icon = "https://openweathermap.org/img/wn/" + current_data["weather"][0]["icon"] + "@2x.png"

    return render_template('results.html', city=city, country=country, temp=temp, feels_like=feels_like, weather=weather, icon=icon,
                            temp0=temp0, icon0=icon0, weather0=weather0, temp1=temp1, icon1=icon1, weather1=weather1, temp2=temp2, 
                            icon2=icon2, weather2=weather2, temp3=temp3, icon3=icon3, weather3=weather3, temp4=temp4, icon4=icon4, 
                            weather4=weather4, temp5=temp5, icon5=icon5, weather5=weather5, temp6=temp6, icon6=icon6, weather6=weather6)


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


    


