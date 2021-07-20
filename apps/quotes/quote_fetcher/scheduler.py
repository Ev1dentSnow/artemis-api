from apscheduler.schedulers.background import BackgroundScheduler

from apps.quotes.quote_fetcher import quote_fetcher


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(quote_fetcher.fetch_quote(), 'interval', hours=23)
    scheduler.start()
    quote_fetcher.fetch_quote()
