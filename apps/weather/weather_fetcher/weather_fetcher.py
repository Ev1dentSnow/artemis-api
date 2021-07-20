import requests
from decouple import config
import json


def fetch_forecast():  # APscheduler does not allow this method to be inside the class

    # Only hardcoded this as it's my high school's latitude and longitude
    lat = -25.7449
    lon = 28.1878
    excluded_data = 'current,hourly,alerts'
    openweathermaps_api_key = config('openweathermapsapikey')
    parameters = {"lat": lat, "lon": lon, "appid": openweathermaps_api_key, "exclude": excluded_data,
                  "units": "metric"}
    result = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)

    with open("apps/weather/weather_data.json", "w") as weather_file:
        weather_file.seek(0)  # Take cursor to beginning of file
        weather_file.truncate()  # Delete the outdated weather data starting at beginning of file
        write_data = result.content.decode('utf-8')
        write_data = write_data.replace('\\', '')
        weather_file.write(write_data)
        weather_file.close()
