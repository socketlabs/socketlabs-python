from .attachment import Attachment
from .bulkrecipient import BulkRecipient
from .customheader import CustomHeader
from .emailaddress import EmailAddress
from .messagebase import MessageBase


class BulkMessage(MessageBase):
    """
    A bulk message usually contains a single recipient per message
    and is generally used to send the same content to many recipients,
    optionally customizing the message via the use of Merge Data.

    :Example:

        message = BulkMessage()

        message.subject = "Sending a tests message"
        message.html_body = "<html><body>" \
                    "<h1>Sending A Test Message</h1>" \
                    "<p>This is the Html Body of my message.</p>" \
                    "</body></html>"
        message.plain_text_body = "This is the Plain Text Body of my message."

        message.from_email_address = EmailAddress("from@example.com")
        message.reply_to = EmailAddress("replyto@example.com")

        message.add_to_recipient("recipient1@example.com")
        message.add_to_recipient("recipient2@example.com", "Recipient #1")
        message.add_to_recipient(BulkRecipient("recipient3@example.com"))
        message.add_to_recipient(BulkRecipient("recipient4@example.com", "Recipient #4"))

        message.add_global_merge_data("name1", "value1")
        message.add_global_merge_data("name2", "value2")

    """

    def __init__(self):
        self._subject = None
        self._plain_text_body = None
        self._html_body = None
        self._api_template = None
        self._mailing_id = None
        self._message_id = None
        self._charset = None
        self._from_email = None
        self._reply_to = None
        self._attachments = []
        self._custom_headers = []
        self._to_recipients = []
        self._global_merge_data = dict()

    @property
    def to_recipient(self):
        """
        Set the To email address list
        :return list of BulkRecipient
        :rtype list
        """
        return self._to_recipients

    @to_recipient.setter
    def to_recipient(self, val: list):
        """
        Get the To email address list
        :param val: list of BulkRecipient
        :rtype val: list
        """
        self._to_recipients = []
        if val is not None:
            for item in val:
                if isinstance(item, BulkRecipient):
                    self._to_recipients.append(item)

    def add_to_recipient(self, email_address, friendly_name: str = None, merge_data: dict = None):
        """
        Add a BulkRecipient to the To recipient list.
        :param email_address: the email address
        :type email_address: object
        :param friendly_name: the recipients friendly name
        :type friendly_name: str
        :param merge_data: merge data for the recipient
        :type merge_data: dict
        """
        if isinstance(email_address, BulkRecipient):
            self._to_recipients.append(email_address)

        if isinstance(email_address, str):
            self._to_recipients.append(BulkRecipient(email_address, friendly_name, merge_data))

    @property
    def global_merge_data(self):
        """
        Get the dictionary containing global merge data items
        :return the dictionary
        :rtype dict
        """
        return self._global_merge_data

    @global_merge_data.setter
    def global_merge_data(self, val: dict):
        """
        Set the dictionary containing global merge data items
        :param val: the dictionary
        :type val: dict
        """
        self._global_merge_data = val

    def add_global_merge_data(self, key: str, val: str):
        """
        Add an entry to the global merge data dictionary
        :param key: the key
        :type val: str
        :param val: the value
        :type val: str
        """
        self._global_merge_data[key] = val

    """
    interface properties
    """

    @property
    def subject(self):
        """
        Get the message subject.
        :return the subject
        :rtype str
        """
        return self._subject

    @subject.setter
    def subject(self, val: str):
        """
        Set the message subject.
        :param val: the subject
        :type val: str
        """
        self._subject = val

    @property
    def plain_text_body(self):
        """
        Get the plain text portion of the message body.
        :return the plain text body
        :rtype str
        """
        return self._plain_text_body

    @plain_text_body.setter
    def plain_text_body(self, val: str):
        """
        Set the plain text portion of the message body.
        :param val: the plain text body
        :type val: str
        """
        self._plain_text_body = val

    @property
    def html_body(self):
        """
        Get the HTML portion of the message body.
        :return the HTML body
        :rtype str
        """
        return self._html_body

    @html_body.setter
    def html_body(self, val: str):
        """
        Set the HTML portion of the message body.
        :param val: the HTML body
        :type val: str
        """
        self._html_body = val

    @property
    def api_template(self):
        """
        Get the api template.
        :return the api template
        :rtype str
        """
        return self._api_template

    @api_template.setter
    def api_template(self, val: str):
        """
        Set the api template.
        :param val: the api template
        :rtype str
        """
        self._api_template = val

    @property
    def mailing_id(self):
        """
        Get the custom mailing id.
        See https://www.injectionapi.com/blog/best-practices-for-using-custom-mailingids-and-messageids/
        for more information.
        :return the mailing id
        :rtype str
        """
        return self._mailing_id

    @mailing_id.setter
    def mailing_id(self, val: str):
        """
        Set the custom mailing id.
        :param val: the mailing id
        :type val: str
        """
        self._mailing_id = val

    @property
    def message_id(self):
        """
        Get the custom message id.
        See https://www.injectionapi.com/blog/best-practices-for-using-custom-mailingids-and-messageids/
        for more information.
        :return the message id
        :rtype str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, val: str):
        """
        Set the custom message id.
        :param val: the message id
        :type val: str
        """
        self._message_id = val

    @property
    def charset(self):
        """
        Get the optional character set. Default is UTF-8
        :return the character set
        :rtype str
        """
        return self._charset

    @charset.setter
    def charset(self, val: str):
        """
        Set the optional character set. Default is UTF-8
        :param val: the character set
        :type val: str
        """
        self._charset = val

    @property
    def from_email_address(self):
        """
        Get the from email address.
        :return EmailAddress
        :rtype EmailAddress
        """
        return self._from_email

    @from_email_address.setter
    def from_email_address(self, val: EmailAddress):
        """
        Set the from email address.
        :param val: EmailAddress
        :type val: EmailAddress
        """
        self._from_email = val

    @property
    def reply_to_email_address(self):
        """
        Get the optional reply to email address
        :return EmailAddress
        :rtype EmailAddress
        """
        return self._reply_to

    @reply_to_email_address.setter
    def reply_to_email_address(self, val: EmailAddress):
        """
        Set the optional reply to email address.
        :param val: EmailAddress
        :type val: EmailAddress
        """
        self._reply_to = val

    @property
    def attachments(self):
        """
        Get the list of Attachments.
        :returns: List of Attachment objects.
        :rtype list
        """
        return self._attachments

    @attachments.setter
    def attachments(self, val: list):
        """
        Set the list of Attachments.
        :param val: list of Attachment
        :type val: list
        """
        self._attachments = []
        if val is not None:
            for item in val:
                if isinstance(item, Attachment):
                    self._attachments.append(item)

    def add_attachment(self, val: Attachment):
        """
        Add an Attachment to the attachments list.
        :param val: list of Attachment
        :type val: list
        """
        self._attachments.append(val)

    @property
    def custom_headers(self):
        """
        Get the list of CustomHeaders.
        :return list of CustomHeader
        :rtype list
        """
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, val: list):
        """
        Set the list of CustomHeaders.
        :param val: list of CustomHeader
        :type val: list
        """
        self._custom_headers = []
        if val is not None:
            for item in val:
                if isinstance(item, CustomHeader):
                    self._custom_headers.append(item)

    def add_custom_header(self, header, val: str = None):
        """
        Add a CustomHeader to the attachment
        :param header: the CustomHeader. CustomHeader, dict, and string is allowed
        :type header: CustomHeader, dict, str
        :param val: the custom header value, required if header is str
        :type val: str
        """
        if isinstance(header, CustomHeader):
            self._custom_headers.append(header)
        if isinstance(header, str):
            self._custom_headers.append(CustomHeader(header, val))
        if isinstance(header, dict):
            for name, value in header.items():
                self._custom_headers.append(CustomHeader(name, value))

    def __str__(self):
        """
        Represents the BulkMessage as a string (# of recipients & subject)
        :return the string
        :rtype str

        """
        return "Recipients: {count}, Subject: '{subject}'" \
            .format(
                count=len(self._to_recipients),
                subject=str(self._subject))
