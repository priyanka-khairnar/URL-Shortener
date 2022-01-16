"""Rest API for URL Shortener."""

from flask import Flask,  jsonify, request, render_template, redirect
from util.logger_utility import LoggerUtility
from util.common_constants import Constants
from shortener.shortener import Shortener
from flask import flash

APP = Flask(__name__)

LoggerUtility.set_level()
shortener = Shortener()


@APP.route('/shortener', methods=['POST'])
def url_shortener():
    """Rest API for URL Shortener."""
    try:
        long_url = request.form['url']
        if not long_url:
            return jsonify({'error': 'Please provide url'}), 400

        response = shortener.url_shortener(long_url)
        LoggerUtility.log_info(response)
        if response:
            # jsonify(short_url=response)
            return render_template("homepage.html", data=response)
        return jsonify({'error': 'Internal Server Error'}), 500
    except AttributeError as exception:
        LoggerUtility.log_error(exception)
        flash(exception)
        return jsonify(exception), 400


@APP.route('/shortener', methods=['GET'])
def home():
    """Rest API for URL Shortener."""
    return render_template("homepage.html")


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
