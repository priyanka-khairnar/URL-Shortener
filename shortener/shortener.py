"""Shortener Service"""


class Shortener():
    def __init__(self):
        """Shortener Initializer"""
        self.short_url = "/dummy_url"
    
    def url_shortener(self, long_url):
        """Function for URL shortener.
            Input: Long URL - String
            Output: Short URL
        """
        return self.short_url