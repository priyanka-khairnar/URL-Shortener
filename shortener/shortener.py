"""Shortener Service"""
import random
import string
from util.common_constants import Constants
from util.file_utility import FileUtility
from util.logger_utility import LoggerUtility

LoggerUtility.set_level()
class Shortener():
    def __init__(self):
        """Shortener Initializer"""
        self.short_url = ""
        self.pre_url = Constants.HOST + ":" + str(Constants.PORT) + "/"
        self.data = self._load_file_data()
        LoggerUtility.log_info('Data: ' + str(self.data))
    
    def url_shortener(self, long_url):
        """Function for URL shortener.
            Input: Long URL - String
            Output: Short URL
        """
        encode = self._encode()
        post_url = FileUtility.write_to_text_file(encode, long_url)
        self.short_url = self.pre_url + post_url
        self.data[post_url] = long_url
        return self.short_url
    
    def _encode(self):
        """Create encoded string to append to short url"""
        sha = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return sha
    
    def get_long_url(self, short_url):
        """Get Long URL"""
        return FileUtility.get_long_url_from_text(short_url)
    
    def _load_file_data(self):
        return FileUtility.load_file_data_as_dict()
    
    def get_long_url_from_cache(self, short_url):
        return self.data.get(short_url, None)