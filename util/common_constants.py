"""Common constants module."""

class Constants:
    """General constants class."""

    LOGGER_NAME = 'consumer'
    DEFAULT_LOG_LEVEL = 'INFO'
    HOST = "localhost"
    PORT = 8000
    TEXT_FILE_NAME = "urls.txt"

    def __setattr__(self, attr, value):
        """Restrict editing constant values."""
        if hasattr(self, attr):
            raise Exception("Attempting to alter read-only value")

        self.__dict__[attr] = value


class EnvironmentVariables:
    """Environment variables constants class."""

    LOG_LEVEL = 'LOG_LEVEL'

    def __setattr__(self, attr, value):
        """Restrict editing constant values."""
        if hasattr(self, attr):
            raise Exception("Attempting to alter read-only value")

        self.__dict__[attr] = value