from urllib.parse import urlparse

class HttpEndpoint(object):
    """
    The HTTP endpoint
    """

    def __init__(self, url: str):
        """
        Create an instance of the HttpEndpoint class
        :param host: the host name
        :type host: str
        :param url: the url
        :type url: str
        """
        parsed_url = urlparse(url)
        self._host = parsed_url.hostname
        self._url = parsed_url.path


    @property
    def url(self):
        """
        Get the HTTP endpoint Url
        :return the url
        :rtype str
        """
        return self._url

    @property
    def host(self):
        """
        Get the HTTP endpoint Host name
        :return the host name
        :rtype str
        """
        return self._host
