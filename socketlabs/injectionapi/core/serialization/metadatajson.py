class MetadataJson(object):
    """
    Represents a metadata as a key and value pair.
    To be serialized into JSON string before sending to the Injection Api.
    """

    def __init__(self, key: str = None, val: str = None):
        """
        Initializes a new instance of the MetadataJson class
        :param key: the key of the metadata
        :type key: str
        :param val: the value of the metadata
        :type val: str
        """
        self._key = key
        self._value = val

    @property
    def key(self):
        """
        The key of the metadata.
        :return the key
        :rtype str
        """
        return str(self._key)

    @key.setter
    def key(self, val: str):
        """
        Set the key of the metadata.
key        :type val: str
        """
        self._key = val

    @property
    def value(self):
        """
        The value of the metadata.
        :return the value
        :rtype str
        """
        return str(self._value)

    @value.setter
    def value(self, val: str):
        """
        Set value of the metadata.
        :param val: the value
        :type val: str
        """
        self._value = val

    def to_json(self):
        """
        build json dict for MetadataJson
        :return the json dictionary
        :rtype dict
        """
        return {
            "key":  self._key,
            "value": self._value
        }
