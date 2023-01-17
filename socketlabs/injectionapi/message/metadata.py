from ..core.stringextension import StringExtension


class Metadata(object):
    """
    Represents a metadata as a key-value pair.

    :Example:

        metadata1 = Metadata()
        metadata1.key = "key1"
        metadata1.value = "value1"

        metadata2 = Metadata("key1", "value1")

    """

    def __init__(self, key: str = None, val: str = None):
        """
        Initializes a new instance of the Metadata class
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
        Get the key
        :return the key
        :rtype str
        """
        return str(self._key)

    @key.setter
    def key(self, val: str):
        """
        Set the key
        :param val: the key
        :type val: str
        """
        self._key = val

    @property
    def value(self):
        """
        Get the value
        :return the value
        :rtype str
        """
        return str(self._value)

    @value.setter
    def value(self, val: str):
        """
        Set the value
        :param val: the value
        :type val: str
        """
        self._value = val

    def isvalid(self):
        """
        Determines if the Metadata is valid.
        :return the result
        :rtype bool
        """
        validkey = not StringExtension.is_none_or_white_space(self._key)
        validvalue = not StringExtension.is_none_or_white_space(self._value)
        if validkey and validvalue:
            return True
        return False

    def __str__(self):
        """
        Represents the Metadata key-value pair as a string
        :return the string
        :rtype str
        """
        return str(self._key + ", " + self._value)
