from injectionapi.core.string_extension import StringExtension


class BulkRecipient(object):
    """
    Represents an individual email address for a BulkMessage

    :Example:

        recipient = BulkRecipient("recipient@example.com", "Recipient 1")
        recipient.add_merge_data("key1", "value1")
        recipient.add_merge_data("key2", "value2")

    """

    def __init__(self, email_address: str = None, friendly_name: str = None, merge_data: dict = None):
        """
        Initializes a new instance of the BulkRecipient class
        :param email_address: the email address
        :type email_address: str
        :param friendly_name: the recipients friendly name
        :type friendly_name: str
        :param merge_data: merge data for the recipient
        :type merge_data: dict
        """
        self._email_address = email_address
        self._friendly_name = friendly_name
        if merge_data is not None:
            self._merge_data = merge_data
        else:
            self._merge_data = dict()

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

    @property
    def merge_data(self):
        """
        Get the dictionary containing merge data items
        :return the dictionary
        :rtype dict
        """
        return self._merge_data

    @merge_data.setter
    def merge_data(self, val: dict):
        """
        Set the dictionary containing merge data items
        :param val: the dictionary
        :type val: dict
        """
        self._merge_data = val

    def add_merge_data(self, key: str, val: str):
        """
        Add an entry to the merge data dictionary
        :param key: the key
        :type val: str
        :param val: the value
        :type val: str
        """
        self._merge_data[key] = val

    def isvalid(self):
        """
        Determines if the BulkRecipient is valid. Does simple syntax validation on the email address.
        :return the result
        :rtype bool
        """
        return StringExtension.is_valid_email_address(self.email_address)

    def __str__(self):
        """
        Represents the BulkRecipient as a string
        :return the BulkRecipient
        :rtype str
        """
        if self._friendly_name:
            return "{name} <{email}>".format(name=self._friendly_name, email=str(self._email_address))
        return str(self._email_address)
