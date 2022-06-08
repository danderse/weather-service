from flask import Flask, make_response
import requests

app = Flask(__name__)

@app.route("/current-weather/<lat>/<lon>")
def fetch_weather(lat, lon):
  apiKey = "5003aab957ef5495752bd28c41b7abd7"
  print(lat)
  uri = "https://api.openweathermap.org/data/3.0/onecall?lat={0}&lon={1}&exclude=minutely,hourly,daily&appid={2}".format(lat, lon, apiKey)
  resp = requests.get(uri)
  if resp.status_code < 300:
    data = resp.json()
    return {
      "condition": [{"main": w.main, "description": w.description} for w in data.current.weather],
      "temp_feels": how_does_temp_feel(data.current.temp),
      "alerts": [{"event": a.event, "description": a.description} for a in data.alerts]
    }
  else:
    return make_response ({
      "status": resp.status_code,
      "error": resp.text
    }, resp.status_code)

def how_does_temp_feel(temp):
  if temp < 50:
    return "cold"
  if temp > 75:
    return "hot"
  return "moderate"

