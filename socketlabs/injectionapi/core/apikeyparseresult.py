from enum import Enum


class ApiKeyParseResult(Enum):
    """
    Enumerated result of parsing the API Key
    """

    """ No result could be produced. """
    NoneSet = 0

    """ The key was found to be blank or invalid. """
    InvalidEmptyOrWhitespace = 1

    """ The public portion of the key was unable to be parsed. """
    InvalidUnableToExtractPublicPart = 2

    """ The secret portion of the key was unable to be parsed. """
    InvalidUnableToExtractSecretPart = 3

    """ Key was successfully parsed. """
    Success = 4

    def __str__(self):
        """
        String representation of the SendResult Enum
        :return the string
        :rtype str
        """
        switcher = {
            0: "No result could be produced.",
            1: "The key was found to be blank or invalid.",
            2: "The public portion of the key was unable to be parsed.",
            3: "The secret portion of the key was unable to be parsed.",
            4: "Key was successfully parsed.",
        }
        return switcher.get(self.value, "An error has occurred that was unforeseen")

    def describe(self):
        """
        string output of the
        :return the string
        :rtype str
        """
        return self.name, self.value, self.__str__
