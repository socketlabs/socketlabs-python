from injectionapi.core.string_extension import StringExtension


class EmailAddress(object):
    """
    Represents an individual email address for a message.

    :Example:

        email_address = EmailAddress("recipient@example.com", "Recipient 1")

    """

    def __init__(self, email_address: str = None, friendly_name: str = None):
        """
        Initializes a new instance of the EmailAddress class
        :param email_address: the email address
        :type email_address: str
        :param friendly_name: the recipients friendly name
        :type friendly_name: str
        """
        self._email_address = email_address
        self._friendly_name = friendly_name

    @property
    def email_address(self):
        """
        Get the email address
        :return the email address
        :rtype val: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, val: str):
        """
        Set the email address
        :param val: the email address
        :type val: str
        """
        self._email_address = val

    @property
    def friendly_name(self):
        """
        Get the friendly or display name
        :return the recipients friendly name
        :rtype str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, val: str):
        """
        Set the friendly or display name
        :param val: the recipients friendly name
        :type val: str
        """
        self._friendly_name = val

    def isvalid(self):
        """
        Determines if the EmailAddress is valid. Does simple syntax validation on the email address.
        :return bool
        """
        return StringExtension.is_valid_email_address(self.email_address)

    def __str__(self):
        """
        Represents the EmailAddress as a string
        :return the EmailAddress
        :rtype str
        """
        if self._friendly_name:
            return "{name} <{email}>".format(name=self._friendly_name, email=str(self._email_address))
        return str(self._email_address)
