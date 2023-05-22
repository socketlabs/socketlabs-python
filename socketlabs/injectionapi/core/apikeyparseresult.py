from enum import Enum


class ApiKeyParseResult(Enum):
    """
    Enumerated result of parsing the API Key
    """

    """ No result could be produced. """
    NoneSet = 0

    """ Invalid key length was found. """
    InvalidKeyLength = 1

    """ Invalid key format was found. """
    InvalidKeyFormat = 2

    """ The key was found to be blank or invalid. """
    InvalidEmptyOrWhitespace = 3

    """ The public portion of the key was unable to be parsed. """
    InvalidUnableToExtractPublicPart = 4

    """ The secret portion of the key was unable to be parsed. """
    InvalidUnableToExtractSecretPart = 5

    """ The public portion of the key is the incorrect length. """
    InvalidPublicPartLength = 6

    """ The secret portion of the key is the incorrect length. """
    InvalidSecretPartLength = 7

    """ Key was successfully parsed. """
    Success = 8

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
