class AddressResult(object):
    """
    The result of a single recipient in the Injection request.
    """

    def __init__(self, email_address: str = None, accepted: bool = None, error_code: str = None):
        """
        Initializes a new instance of the AddressResult class
        :param email_address: The recipient's email address.
        :type email_address: str
        :param accepted: Whether the recipient was accepted for delivery.
        :type  accepted: bool
        :param error_code: An error code detailing why the recipient was not accepted.
        :type error_code: str
        """
        self._email_address = email_address
        self._accepted = accepted
        self._error_code = error_code

    @property
    def email_address(self):
        """
        Get the recipient's email address.
        :return the recipient's email address.
        :rtype str
        """
        return str(self._email_address)

    @email_address.setter
    def email_address(self, val: str):
        """
        Set the recipient's email address.
        :param val: the recipient's email address.
        :type val: str
        """
        self._email_address = val

    @property
    def accepted(self):
        """
       Get whether the recipient was accepted for delivery.
        :return whether the recipient was accepted
        :rtype bool
        """
        return str(self._accepted)

    @accepted.setter
    def accepted(self, val: bool):
        """
        Set whether the recipient was accepted for delivery.
        :param val: whether the recipient was accepted
        :type val: bool
        """
        self._accepted = val

    @property
    def error_code(self):
        """
        Get an error code detailing why the recipient was not accepted.
        :return an error code
        :rtype str
        """
        return str(self._error_code)

    @error_code.setter
    def error_code(self, val: str):
        """
        Set an error code detailing why the recipient was not accepted.
        :param val: an error code
        :type val: str
        """
        self._error_code = val

    def __str__(self):
        """
        Represents the AddressResult as a str.  Useful for debugging.
        :return the string
        :rtype str
        """
        return "{error_code}: {email_address}"\
            .format(
                error_code=self._error_code,
                email_address=self._email_address)

    def to_json(self):
        """
        build json dict for AddressResult
        :return the json dictionary
        :rtype dict
        """
        return {
            "errorCode": self._error_code,
            "accepted": self._accepted,
            "emailAddress": self._email_address
        }
