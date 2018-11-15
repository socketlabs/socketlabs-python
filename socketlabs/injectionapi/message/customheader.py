from ..core.stringextension import StringExtension


class CustomHeader(object):
    """
    Represents a custom header as a name-value pair.

    :Example:

        header1 = CustomHeader()
        header1.name = "name1"
        header1.value = "value1"

        header2 = CustomHeader("name1", "value1")

    """

    def __init__(self, name: str = None, val: str = None):
        """
        Initializes a new instance of the CustomHeader class
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
        Determines if the CustomHeader is valid.
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
        Represents the CustomHeader name-value pair as a string
        :return the string
        :rtype str
        """
        return str(self._name + ", " + self._value)
