from django.apps import AppConfig


class QuotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.quotes'

    # This method runs automagically when the app starts (called by Django)
    def ready(self):
        from apps.quotes.quote_fetcher import scheduler
        scheduler.start()
