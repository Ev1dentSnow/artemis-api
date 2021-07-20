from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from apps.weather.weather_fetcher import weather_fetcher
from apps.weather.weather_fetcher.weather_fetcher import fetch_forecast


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(weather_fetcher.fetch_forecast, 'interval', minutes=60)
    scheduler.start()
    fetch_forecast()
