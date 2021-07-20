from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.weather'

    # This method runs automagically when the app starts (called by Django)
    def ready(self):
        from apps.weather.weather_fetcher import scheduler
        scheduler.start()
