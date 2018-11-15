class HttpEndpoint(object):
    """
    The HTTP endpoint
    """

    def __init__(self, host: str = None, url: str = None):
        """
        Create an instance of the HttpEndpoint class
        :param host: the host name
        :type host: str
        :param url: the url
        :type url: str
        """
        self._host = host
        self._url = url

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
