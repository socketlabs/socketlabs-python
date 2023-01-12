from ..core.stringextension import StringExtension


class Metadata(object):
    """
    Represents a metadata as a name-value pair.

    :Example:

        metadata1 = Metadata()
        metadata1.name = "name1"
        metadata1.value = "value1"

        metadata2 = Metadata("name1", "value1")

    """

    def __init__(self, name: str = None, val: str = None):
        """
        Initializes a new instance of the Metadata class
        :param name: the name of the metadata
        :type name: str
        :param val: the value of the metadata
        :type val: str
        """
        self._name = name
        self._value = val

    @property
    def name(self):
        """
        Get the name
        :return the name
        :rtype str
        """
        return str(self._name)

    @name.setter
    def name(self, val: str):
        """
        Set the name
        :param val: the name
        :type val: str
        """
        self._name = val

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
        validName = not StringExtension.is_none_or_white_space(self._name)
        validValue = not StringExtension.is_none_or_white_space(self._value)
        if validName and validValue:
            return True
        return False

    def __str__(self):
        """
        Represents the Metadata name-value pair as a string
        :return the string
        :rtype str
        """
        return str(self._name + ", " + self._value)
