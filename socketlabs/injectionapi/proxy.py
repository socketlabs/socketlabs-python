class Proxy(object):
    """
    Represents a http proxy.
    """

    def __init__(self, host: str = None, port: int = None):
        """
        Initializes a new instance of the Proxy class
        :param host: proxy host name
        :type host : str
        :param port: proxy port
        :type port : int
        """
        self._host = host
        self._port = port

    @property
    def host(self):
        """
        The name of the proxy hostname
        :return the proxy hostname
        :rtype str
        """
        return self._host

    @host.setter
    def host(self, val: str):
        """
        Set the name of the proxy hostname
        :param val: the proxy hostname
        :type val: str
        """
        self._host = val

    @property
    def port(self):
        """
        The value of the proxy port
        :return the proxy port
        :rtype str
        """
        return self._port

    @port.setter
    def port(self, val: str):
        """
        Get the value of the proxy port
        :param val: the proxy port
        :type val: str
        """
        self._port = val

    def __str__(self):
        """
        Returns the Proxy as a string.
        :return the string
        :rtype str
        """
        return str(self._host + ":" + self._port)
