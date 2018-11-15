class CustomHeaderJson(object):
    """
    Represents a custom header as a name and value pair.
    To be serialized into JSON string before sending to the Injection Api.
    """

    def __init__(self, name: str = None, val: str = None):
        """
        Initializes a new instance of the CustomHeaderJson class
        :param name: the name of the custom header
        :type name: str
        :param val: the value of the custom header
        :type val: str
        """
        self._name = name
        self._value = val

    @property
    def name(self):
        """
        The name of the custom header.
        :return the name
        :rtype str
        """
        return str(self._name)

    @name.setter
    def name(self, val: str):
        """
        Set the name of the custom header.
        :param val: the name
        :type val: str
        """
        self._name = val

    @property
    def value(self):
        """
        The value of the custom header.
        :return the value
        :rtype str
        """
        return str(self._value)

    @value.setter
    def value(self, val: str):
        """
        Set value of the custom header.
        :param val: the value
        :type val: str
        """
        self._value = val

    def to_json(self):
        """
        build json dict for CustomHeaderJson
        :return the json dictionary
        :rtype dict
        """
        return {
            "name":  self._name,
            "value": self._value
        }
