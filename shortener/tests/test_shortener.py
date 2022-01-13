import pytest
from mock import MagicMock
import sys

class TestShortener(object):
    def test_shortener(self):
        """Test shortener Service
            Input: Long URL
            Output: Short URL
        """
        pass
    
    def test_same_url(self):
        """Test for the same URL to verify service is not generating Short URL again
            Input: Long URL
            Output: Short URL
        """
        pass
    
    def test_invalid_url(self):
        """Test for invalid URL
            Input: Invalid URL
            Output: Invalid URL Error Response
        """
        pass
    
    