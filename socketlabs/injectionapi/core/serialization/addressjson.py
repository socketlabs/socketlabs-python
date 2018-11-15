class AddressJson(object):
    """
    Represents an individual email address for a message.
    To be serialized into JSON string before sending to the Injection Api.
    """

    def __init__(self, email_address: str = None, friendly_name: str = None):
        """
        Initializes a new instance of the AddressJson class
        :param email_address: the email address
        :type email_address: str
        :param friendly_name: the recipients friendly name
        :type friendly_name: str
        """
        self._email_address = email_address
        self._friendly_name = friendly_name

    @property
    def email(self):
        """
        Get the email address
        :return the email address
        :rtype val: str
        """
        return str(self._email_address)

    @email.setter
    def email(self, val: str):
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
        return str(self._friendly_name)

    @friendly_name.setter
    def friendly_name(self, val: str):
        """
        Set the friendly or display name
        :param val: the recipients friendly name
        :type val: str
        """
        self._friendly_name = val

    def to_json(self):
        """
        build json dict for AddressJson
        :return the json dictionary
        :rtype dict
        """
        if self._friendly_name is not None and self._friendly_name.strip() != '':
            return {
                "emailAddress":  self._email_address,
                "friendlyName": self._friendly_name
            }
        return {
                "emailAddress":  self._email_address
            }
