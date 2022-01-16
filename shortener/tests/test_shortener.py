import pytest
from shortener.shortener import Shortener


shortener = Shortener()
class TestShortener(object):
    def test_shortener(self):
        """Test shortener Service
            Input: Long URL
            Output: Short URL
        """
        long_url = "https://www.google.com/search?q=url+shortner&rlz=1C1CHBF_enIN979IN979&oq=url+shortner&aqs=chrome..69i57j0i10i433j69i59j0i10i433l2j69i60l3.3777j0j7&sourceid=chrome&ie=UTF-8"
        short_url = shortener.url_shortener(long_url)
        assert short_url != None

    def test_same_url(self):
        """Test for the same URL to verify service is not generating Short URL again
            Input: Long URL
            Output: Short URL
        """
        long_url = "https://www.google.com/search?q=pytest&rlz=1C1CHBF_enIN979IN979&sxsrf=AOaemvJBiNK6kFB9TlFHSOSYLYgDfMElMQ%3A1642337059243&ei=IxPkYbCdDobb2roPgru2aA&ved=0ahUKEwjwupGoprb1AhWGrVYBHYKdDQ0Q4dUDCA4&uact=5&oq=pytest&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEJECMgQIABBDMgUIABCABDIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOg0ILhDHARDRAxCwAxBDOgoIABCxAxCDARBDOgoILhDHARDRAxBDOggILhCxAxCDAToICAAQgAQQsQM6CwguEIAEELEDEIMBOg0IABCABBCHAhCxAxAUOg0ILhCxAxDHARDRAxAKOgcIABCxAxAKOgcIABCxAxBDSgQIQRgASgQIRhgAUJoLWIATYPEVaAFwAXgAgAHTAogB7weSAQcwLjUuMC4xmAEAoAEByAEKwAEB&sclient=gws-wiz"
            
        short_url_1 = shortener.url_shortener(long_url)
        short_url_2 = shortener.url_shortener(long_url)
        assert short_url_1 == short_url_2

    def test_invalid_url(self):
        """Test for invalid URL
            Input: Invalid URL
            Output: Invalid URL Error Response
        """
        pass
