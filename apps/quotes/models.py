from django.db import models


class Quote:

    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    @property
    def quote(self):
        return self.quote

    @quote.setter
    def quote(self, quote):
        self.quote = quote

    @property
    def author(self):
        return self.author

    @author.setter
    def author(self, author):
        self.author = author