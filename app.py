"""Rest API for URL Shortener."""

from urllib import response
from flask import Flask,  jsonify, request, render_template, redirect
from util.logger_utility import LoggerUtility
from util.common_constants import Constants
from shortener.shortener import Shortener
from flask import flash
import json

APP = Flask(__name__)

LoggerUtility.set_level()
shortener = Shortener()


@APP.route('/shortener', methods=['GET', 'POST'])
def url_shortener():
    """Rest API for URL Shortener."""
    try:
        if request.method == 'GET':
            return render_template("homepage.html")
        elif request.method == 'POST':
            data = json.loads(request.data)
            long_url = data.get('url')
            if not long_url:
                return jsonify({'error': 'Please provide url'}), 400

            short_url = shortener.url_shortener(long_url)
            LoggerUtility.log_info(short_url)
            if short_url:
                # jsonify(response), 200
                response = APP.response_class(
                    response=json.dumps({'short_url': short_url}),
                    status=200,
                    mimetype='application/json'
                )
                # return jsonify(json.dumps({'short_url': short_url})), 200
                return response
            return jsonify({'error': 'Internal Server Error'}), 500
    except AttributeError as exception:
        LoggerUtility.log_error(exception)
        flash(exception)
        return jsonify(exception), 400


# @APP.route('/shortener', methods=['GET'])
# def home():
#     """Rest API for URL Shortener."""
    


@APP.route('/<shorturl>', methods=['GET'])
def redirect_long_url(shorturl):
    """Rest API for URL Shortener."""
    LoggerUtility.log_info('Short URL requested: ' + shorturl)
    long_url = shortener.get_long_url_from_cache(shorturl)
    if long_url:
        LoggerUtility.log_info('Returning Long URL: ' + long_url)
        return redirect(long_url)
    else:
        return jsonify('Long URL not found!'), 400


if __name__ == '__main__':
    # APP.run(host=Constants.HOST, port=Constants.PORT, debug=True)
    APP.run(host='0.0.0.0', port=5001, debug=True)
