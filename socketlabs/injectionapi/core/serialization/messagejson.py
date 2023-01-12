from .addressjson import AddressJson
from .attachmentjson import AttachmentJson
from .customheaderjson import CustomHeaderJson
from .mergedatajson import MergeDataJson
from .metadatajson import MetadataJson


class MessageJson(object):
    """
    Represents a message for sending to the Injection Api.
    To be serialized into JSON string before sending to the Injection Api.
    """

    def __init__(self):
        self._subject = None
        self._plain_text_body = None
        self._html_body = None
        self._amp_body = None
        self._api_template = None
        self._mailing_id = None
        self._message_id = None
        self._charset = None
        self._from_email = None
        self._reply_to = None
        self._attachments = []
        self._custom_headers = []
        self._to_email_address = []
        self._cc_email_address = []
        self._bcc_email_address = []
        self._merge_data = None
        self._metadata = []
        self._tags = []

    @property
    def to_email_address(self):
        """
        Set the To email address list
        :return list of AddressJson
        :rtype list
        """
        return self._to_email_address

    @to_email_address.setter
    def to_email_address(self, val: list):
        """
        Get the To email address list
        :param val: list of AddressJson
        :rtype val: list
        """
        self._to_email_address = []
        if val is not None:
            for item in val:
                if isinstance(item, AddressJson):
                    self._to_email_address.append(item)

    @property
    def cc_email_address(self):
        """
        Set the CC email address list
        :return list of AddressJson
        :rtype list
        """
        return self._cc_email_address

    @cc_email_address.setter
    def cc_email_address(self, val: list):
        """
        Set the CC email address list
        :param val: list of AddressJson
        :rtype val: list
        """
        self._cc_email_address = []
        if val is not None:
            for item in val:
                if isinstance(item, AddressJson):
                    self._cc_email_address.append(item)

    @property
    def bcc_email_address(self):
        """
        Set the BCC email address list
        :return list of AddressJson
        :rtype list
        """
        return self._bcc_email_address

    @bcc_email_address.setter
    def bcc_email_address(self, val: list):
        """
        Set the BCC email address list
        :param val: list of AddressJson
        :rtype val: list
        """
        self._bcc_email_address = []
        if val is not None:
            for item in val:
                if isinstance(item, AddressJson):
                    self._bcc_email_address.append(item)

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
    def amp_body(self):
        """
        Get the AMP portion of the message body.
        :return the AMP body
        :rtype str
        """
        return self._amp_body

    @amp_body.setter
    def amp_body(self, val: str):
        """
        Set the AMP portion of the message body.
        :param val: the AMP body
        :type val: str
        """
        self._amp_body = val

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
        :return AddressJson
        :rtype AddressJson
        """
        return self._from_email

    @from_email_address.setter
    def from_email_address(self, val: AddressJson):
        """
        Set the from email address.
        :param val: AddressJson
        :type val: AddressJson
        """
        self._from_email = val

    @property
    def reply_to_email_address(self):
        """
        Get the optional reply to email address.
        :return AddressJson
        :rtype AddressJson
        """
        return self._reply_to

    @reply_to_email_address.setter
    def reply_to_email_address(self, val: AddressJson):
        """
        Set the optional reply to address.
        :param val: AddressJson
        :type val: AddressJson
        """
        self._reply_to = val

    @property
    def attachments(self):
        """
        Get the list of attachments.
        :returns: List of AttachmentJson objects.
        :rtype list
        """
        return self._attachments

    @attachments.setter
    def attachments(self, val: list):
        """
        Set the list of AttachmentJson.
        :param val: list of AttachmentJson
        :type val: list
        """
        self._attachments = []
        if val is not None:
            for item in val:
                if isinstance(item, AttachmentJson):
                    self._attachments.append(item)

    def add_attachment(self, val: AttachmentJson):
        """
        Add an AttachmentJson to the attachments list.
        :param val: list of AttachmentJson
        :type val: list
        """
        self._attachments.append(val)

    @property
    def custom_headers(self):
        """
       Get the list of CustomHeaderJson.
        :return list of CustomHeaderJson
        :rtype list
        """
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, val: list):
        """
        Set the list of CustomHeaderJson.
        :param val: list of CustomHeaderJson
        :type val: list
        """
        self._custom_headers = []
        if val is not None:
            for item in val:
                if isinstance(item, CustomHeaderJson):
                    self._custom_headers.append(item)

    def add_custom_header(self, name: str, val: str):
        """
        Add a CustomHeaderJson to the custom header list
        :param name: the name
        :type val: str
        :param val: the value
        :type val: str
        """
        self._custom_headers.append(CustomHeaderJson(name, val))

    @property
    def merge_data(self):
        """
        Get the the list of MergeDataJson
        :return list of MergeDataJson
        :rtype list

        """
        return self._merge_data

    @merge_data.setter
    def merge_data(self, val: MergeDataJson):
        """
        Set the the list of MergeDataJson
        :param val: list of MergeDataJson
        :type val: list
        """
        self._merge_data = val


    @property
    def metadata(self):
        """
       Get the list of MetadataJson.
        :return list of MetadataJson
        :rtype list
        """
        return self._metadata

    @metadata.setter
    def metadata(self, val: list):
        """
        Set the list of MetadataJson.
        :param val: list of MetadataJson
        :type val: list
        """
        self._metadata = []
        if val is not None:
            for item in val:
                if isinstance(item, MetadataJson):
                    self._metadata.append(item)

    def add_metadata(self, name: str, val: str):
        """
        Add a MetadataJson to the metadata list
        :param name: the name
        :type val: str
        :param val: the value
        :type val: str
        """
        self._metadata.append(MetadataJson(name, val))

    @property
    def tags(self):
        """
       Get the list of tags.
        :return list of tags
        :rtype list
        """
        return self._tags

    @tags.setter
    def tags(self, val: list):
        """
        Set the list of tags.
        :param val: list of tags
        :type val: list
        """
        self._tags = []
        if val is not None:
            for item in val:
                self._tags.append(item)

    def add_tags(self, val: str):
        """
        Add a string to the tags list
        :param val: the value
        :type val: str
        """
        self._tags.append(val)

    def to_json(self):
        """
        build json dict for MessageJson
        :return the json dictionary
        :rtype dict
        """

        json = {
            "from": self.from_email_address.to_json()
        }

        if self.subject is not None and self.subject.strip() != '':
            json["subject"] = self.subject

        if self.html_body is not None and self.html_body.strip() != '':
            json["htmlBody"] = self.html_body

        if self.amp_body is not None and self._amp_body.strip() != '':
            json["ampBody"] = self.amp_body

        if self.plain_text_body is not None and self.plain_text_body.strip() != '':
            json["textBody"] = self.plain_text_body

        if self.api_template is not None and self.api_template.strip() != '':
            json["apiTemplate"] = self.api_template

        if self.mailing_id is not None and self.mailing_id.strip() != '':
            json["mailingId"] = self.mailing_id

        if self.message_id is not None and self.message_id.strip() != '':
            json["messageId"] = self.message_id

        if self._reply_to is not None:
            json["replyTo"] = self._reply_to.to_json()

        if self.charset is not None and self.charset.strip() != '':
            json["charSet"] = self.charset

        if len(self.to_email_address) > 0:
            e = []
            for i in self.to_email_address:
                e.append(i.to_json())
            json["to"] = e

        if len(self.cc_email_address) > 0:
            e = []
            for i in self.cc_email_address:
                e.append(i.to_json())
            json["cc"] = e

        if len(self.bcc_email_address) > 0:
            e = []
            for i in self.bcc_email_address:
                e.append(i.to_json())
            json["bcc"] = e

        if len(self.custom_headers) > 0:
            e = []
            for i in self.custom_headers:
                e.append(i.to_json())
            json["customHeaders"] = e

        if len(self.attachments) > 0:
            e = []
            for i in self.attachments:
                e.append(i.to_json())
            json["attachments"] = e

        if self.merge_data:
            json["mergeData"] = self.merge_data.to_json()

        if len(self.metadata) > 0:
            e = []
            for i in self.metadata:
                e.append(i.to_json())
            json["metadata"] = e

        if len(self.tags) > 0:
            json["tags"] = self.tags

        return json
