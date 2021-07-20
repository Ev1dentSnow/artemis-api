import json

import requests

from apps.quotes import models


def fetch_quote():

    result = requests.get('https://zenquotes.io/api/today')   # Fetches the quote of the day from the zenquotes API
    result_json = result.json()
    with open('apps/quotes/daily_quote.json', 'w') as quote_file:
        quote_file.seek(0)
        quote_file.truncate()
        quote_file.write(json.dumps(result_json))
        quote_file.close()

