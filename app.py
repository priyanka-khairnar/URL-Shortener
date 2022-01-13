"""Rest API for URL Shortener."""
from chalice import Chalice
from chalice import Response
from util.logger_utility import LoggerUtility
from shortener import Shortener

APP = Chalice(app_name='referenceData')

@APP.route('/shortener', methods=['POST'])
def url_shortener():
    """Rest API for URL Shortener."""
    try:
        request = APP.current_request
        shortener = Shortener()
        response = shortener.url_shortener(request.json_body)
        LoggerUtility.log_info(response)
        if response:
            return Response(body=response, status_code=200)
        return Response(body='Internal Server Error', status_code=500)
    except AttributeError as exception:
        LoggerUtility.log_error(exception)
        return Response(exception, 400)