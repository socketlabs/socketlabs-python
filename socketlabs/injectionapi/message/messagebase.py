from abc import ABCMeta, abstractmethod

from .attachment import Attachment
from .emailaddress import EmailAddress


class MessageBase (metaclass=ABCMeta):
    """
    The MessageBase is an interface that contains fields used by the Injection API
    and is implemented by all message types.
    """

    @property
    @abstractmethod
    def subject(self):
        """
        Get the instance of the message Subject.
        :return the subject
        :rtype str
        """
        pass

    @subject.setter
    @abstractmethod
    def subject(self, val: str):
        """
        Set the instance of the message Subject.
        :param val: the subject
        :type val: str
        """
        pass

    @property
    @abstractmethod
    def plain_text_body(self):
        """
        Get the plain text portion of the message body.
        :return the plain text body
        :rtype str
        """
        pass

    @plain_text_body.setter
    @abstractmethod
    def plain_text_body(self, val: str):
        """
        Set the plain text portion of the message body.
        :param val: the plain text body
        :type val: str
        """
        pass

    @property
    @abstractmethod
    def html_body(self):
        """
        Get the HTML portion of the message body.
        :return the HTML body
        :rtype str
        """
        pass

    @html_body.setter
    @abstractmethod
    def html_body(self, val: str):
        """
        Set the HTML portion of the message body.
        :param val: the HTML body
        :type val: str
        """
        pass

    @property
    @abstractmethod
    def amp_body(self):
        """
        Get the AMP portion of the message body.
        :return the AMP body
        :rtype str
        """
        pass

    @amp_body.setter
    @abstractmethod
    def amp_body(self, val: str):
        """
        Set the AMP portion of the message body.
        :param val: the AMP body
        :type val: str
        """
        pass

    @property
    @abstractmethod
    def api_template(self):
        """
        Get the Api Template for the message.
        :return the api template
        :rtype str
        """
        pass

    @api_template.setter
    @abstractmethod
    def api_template(self, val: str):
        """
        Set the Api Template for the message.
        :param val: the api template
        :rtype str
        """
        pass

    @property
    @abstractmethod
    def mailing_id(self):
        """
        Get the custom MailingId for the message.
        See https://www.injectionapi.com/blog/best-practices-for-using-custom-mailingids-and-messageids/
        for more information.
        :return the mailing id
        :rtype str
        """
        pass

    @mailing_id.setter
    @abstractmethod
    def mailing_id(self, val: str):
        """
        Set the custom MailingId for the message.
        :param val: the mailing id
        :type val: str
        """
        pass

    @property
    @abstractmethod
    def message_id(self):
        """
        Get the custom MessageId for the message.
        See https://www.injectionapi.com/blog/best-practices-for-using-custom-mailingids-and-messageids/
        for more information.
        :return the message id
        :rtype str
        """
        pass

    @message_id.setter
    @abstractmethod
    def message_id(self, val: str):
        """
        Set the custom MessageId for the message.
        :param val: the message id
        :type val: str
        """
        pass

    @property
    @abstractmethod
    def charset(self):
        """
        Get the optional character set. Default is UTF-8
        :return the character set
        :rtype str
        """
        pass

    @charset.setter
    @abstractmethod
    def charset(self, val: str):
        """
        Set the optional character set. Default is UTF-8
        :param val: the character set
        :type val: str
        """
        pass

    @property
    @abstractmethod
    def from_email_address(self):
        """
        Get the From email address.
        :return EmailAddress
        :rtype EmailAddress
        """
        pass

    @from_email_address.setter
    @abstractmethod
    def from_email_address(self, val: EmailAddress):
        """
        Set the From email address.
        :param val: EmailAddress
        :type val: EmailAddress
        """
        pass

    @property
    @abstractmethod
    def reply_to_email_address(self):
        """
        Get the optional reply to  email address for the message.
        :return EmailAddress
        :rtype EmailAddress
        """
        pass

    @reply_to_email_address.setter
    @abstractmethod
    def reply_to_email_address(self, val: EmailAddress):
        """
        Set the optional reply to address for the message.
        :param val: EmailAddress
        :type val: EmailAddress
        """
        pass

    @property
    @abstractmethod
    def attachments(self):
        """
        Get the list of attachments.
        :returns: List of Attachment objects.
        :rtype list
        """
        pass

    @attachments.setter
    @abstractmethod
    def attachments(self, val: list):
        """
        Add an attachment to the attachments list.
        :param val: list of Attachment
        :type val: list
        """
        pass

    @abstractmethod
    def add_attachment(self, val: Attachment):
        """
        Add an attachment to the attachments list.
        :param val: list of Attachment
        :type val: list
        """
        pass

    @property
    @abstractmethod
    def custom_headers(self):
        """
        Get the list of custom message headers added to the message.
        :return list of CustomHeader
        :rtype list
        """
        pass

    @custom_headers.setter
    @abstractmethod
    def custom_headers(self, val: list):
        """
        Set the list of custom message headers added to the message.
        :param val: list of CustomHeader
        :type val: list
        """
        pass
