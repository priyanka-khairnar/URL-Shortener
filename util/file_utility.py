"""Utility module for handleling file."""
import os
from util.common_constants import Constants
from util.logger_utility import LoggerUtility

LoggerUtility.set_level()


class FileUtility:

    @staticmethod
    def write_to_text_file(short_url, long_url):
        """Append Short URL to Text File.
            Input: Short, Long URL 
            Output: If long url exists then from file else add new
        """
        urls = FileUtility.get_from_text_file(long_url, 'POST')
        print(urls)
        if len(urls) == 0:
            with open(Constants.TEXT_FILE_NAME, 'a+') as file:
                content = short_url + "-> " + long_url
                file.write(content + '\n')
            return short_url
        else:
            return urls[0]
        
    @staticmethod
    def get_long_url_from_text(short_url):
        """Get Long URL from Text File
            Input: Short URL to query
            Output: Long URL 
        """
        urls = FileUtility.get_from_text_file(short_url, 'GET')
        if len(urls) != 0:
            return urls[1].strip('\n')
        else:
            LoggerUtility.log_warning("Long URL not found!")
            return None

    @staticmethod 
    def get_from_text_file(match_case, method):
        """Get URLs from Text File
            Input: match_case: condition for fetching URLs
                   method: GET/POST, to identify which type is requested(long_url or short_url)
            Output: URLs, comma separated List, 0 - Short URL, 1 - Long URL
        """
        if os.path.exists(Constants.TEXT_FILE_NAME):
            with open(Constants.TEXT_FILE_NAME, "r") as file:
                if method == 'GET':
                    print('Query for matchcase in GET: ', match_case)
                    matched_line = [line for line in file if line.startswith(match_case)]
                elif method == 'POST':
                    print('Query for matchcase in POST: ', match_case)
                    matched_line = [line for line in file if line.strip('\n').endswith(match_case)]
                else:
                    raise Exception("Wrong method entered!")
                if len(matched_line) != 0:
                    urls = matched_line[0].split("-> ")
                    return urls
                else:
                    return []
        else:
            return []
        
    @staticmethod
    def load_file_data_as_dict():
        """"""
        data = {}
        if os.path.exists(Constants.TEXT_FILE_NAME):
            with open(Constants.TEXT_FILE_NAME, "r") as file:
                for line in file:
                    urls = line.split("-> ")
                    data[urls[0]] = urls[1].strip('\n')
            return data
        else:
            return data
