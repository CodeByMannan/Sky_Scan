from flask import Flask , request , render_template
import requests
app = Flask(__name__)
#paste here ypur api key 
api_key = "65497a62a2ecfded5a796e77593527da"



@app.route("/" , methods = ['GET', 'POST'])
def index():
    variable = None
    if request.method == "POST":
        city = request.form.get("key")
        if city:
            variable =  weather_get(city)
    
    return render_template("index.html" , date = variable)

def weather_get(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    few = {
        'q': city,
        'appid': api_key
    }
    res = requests.get(url , params=few).json()
    return res
    
if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0', port=5000)