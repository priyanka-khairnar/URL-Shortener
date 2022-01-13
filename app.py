"""Rest API for URL Shortener."""
	
from flask import Flask,  jsonify, request
from util.logger_utility import LoggerUtility
from shortener.shortener import Shortener

APP = Flask(__name__)

@APP.route('/shortener', methods=['POST'])
def url_shortener():
    """Rest API for URL Shortener."""
    try:
        long_url = request.json.get('url')
        if not long_url:
            return jsonify({'error': 'Please provide url'}), 400
        shortener = Shortener()
        response = shortener.url_shortener(long_url)
        LoggerUtility.log_info(response)
        if response:
            return response
        return jsonify({'error': 'Internal Server Error'}), 500
    except AttributeError as exception:
        LoggerUtility.log_error(exception)
        return jsonify(exception), 400
    
if __name__ == '__main__':
    APP.run(debug = True)