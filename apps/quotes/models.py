from django.db import models


class Quote:

    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    @property
    def quote(self):
        return self._quote

    @quote.setter
    def quote(self, quote):
        self._quote = quote

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author
