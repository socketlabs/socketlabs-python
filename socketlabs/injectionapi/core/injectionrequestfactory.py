from ..core.serialization.addressjson import AddressJson
from ..core.serialization.attachmentjson import AttachmentJson
from ..core.serialization.customheaderjson import CustomHeaderJson
from ..core.serialization.injectionrequest import InjectionRequest
from ..core.serialization.mergedatajson import MergeDataJson
from ..core.serialization.mergefieldjson import MergeFieldJson
from ..core.serialization.messagejson import MessageJson
from ..message.basicmessage import BasicMessage
from ..message.bulkmessage import BulkMessage
from ..message.bulkrecipient import BulkRecipient
from ..message.emailaddress import EmailAddress
from ..message.messagebase import MessageBase


def email_address_to_address_json(address: EmailAddress):
    """
    Simple converter from EmailAddress to AddressJson
    :param address: the EmailAddress object to convert
    :type address: EmailAddress
    :return the converted AddressJson object
    :rtype AddressJson
    """
    if address.friendly_name is not None and address.friendly_name.strip() != '':
        return AddressJson(address.email_address, address.friendly_name)
    else:
        return AddressJson(address.email_address)


def bulk_recipient_to_address_json(address: BulkRecipient):
    """
    Simple converter from BulkRecipient to AddressJson
    :param address: the BulkRecipient object to convert
    :type address: BulkRecipient
    :return the converted AddressJson object
    :rtype AddressJson
    """
    if address.friendly_name is not None and address.friendly_name.strip() != '':
        return AddressJson(address.email_address, address.friendly_name)
    else:
        return AddressJson(address.email_address)


def populate_custom_headers(custom_headers: list):
    """
    Converts a List of CustomHeader objects to a List of CustomHeaderJson objects.
    :param custom_headers: list of CustomHeader to convert
    :type custom_headers: list
    :return the converted list of CustomHeaderJson
    :rtype list
    """
    if custom_headers is None:
        return None
    custom_header_json = []
    for item in custom_headers:
        custom_header_json.append(CustomHeaderJson(item.name, item.value))
    return custom_header_json


def populate_attachments(attachments: list):
    """
    Converts a list of Attachment objects to a List of AttachmentJson objects.
    :param attachments: list of Attachment to convert
    :type attachments: list
    :return the converted list of AttachmentJson
    :rtype list
    """
    if attachments is None:
        return None
    attachment_json = []
    for item in attachments:
        at_json = AttachmentJson()
        at_json.name = item.name
        at_json.mime_type = item.mime_type
        at_json.content_id = item.content_id
        at_json.content = item.content
        at_json.custom_headers = populate_custom_headers(item.custom_headers)
        attachment_json.append(at_json)
    return attachment_json


def populate_email_list(addresses: list):
    """
    Converts a List of EmailAddress objects to a List of AddressJson objects.
    :param addresses: list of EmailAddress to convert
    :type addresses: list
    :return the converted list of AddressJson
    :rtype list
    """
    if addresses is None:
        return None
    addresses_json = []
    for item in addresses:
        addresses_json.append(email_address_to_address_json(item))
    return addresses_json


def generate_merge_field_list(merge_data: dict):
    """
    Converts a dictionary of merge data into a List of MergeFieldJson objects.
    :param merge_data: dict to convert
    :type merge_data: dict
    :return the converted list of MergeFieldJson
    :rtype list
    """
    merge_field_json = []
    for key in merge_data:
        json = MergeFieldJson(key, merge_data[key])
        merge_field_json.append(json)
    return merge_field_json


def populate_merge_data(global_md: dict, recipients: list):
    """
    Populates global merge data and per message merge data to a MergeDataJson.
    :param global_md: dict of global merge data to convert
    :type global_md: dict
    :param recipients: list of BulkRecipients to convert
    :type recipients: list
    :return the converted MergeDataJson object
    :rtype MergeDataJson
    """
    per_message_mf = []
    global_mf = generate_merge_field_list(global_md)
    for item in recipients:
        merge_field_json = generate_merge_field_list(item.merge_data)
        merge_field_json.append(MergeFieldJson("DeliveryAddress", item.email_address))
        if item.friendly_name:
            merge_field_json.append(MergeFieldJson("RecipientName", item.friendly_name))
        per_message_mf.append(merge_field_json)
    return MergeDataJson(per_message_mf, global_mf)


def generate_base_message(message: MessageBase):
    """
    Converts MessageBase object to a MessageJson object
    :param message: the message to convert
    :type message: MessageBase
    :return the convert MessageJson object
    :rtype MessageJson
    """
    message_json = MessageJson()
    message_json.subject = message.subject
    message_json.plain_text_body = message.plain_text_body
    message_json.html_body = message.html_body
    message_json.mailing_id = message.mailing_id
    message_json.message_id = message.message_id
    message_json.charset = message.charset
    message_json.from_email_address = email_address_to_address_json(message.from_email_address)
    message_json.custom_headers = populate_custom_headers(message.custom_headers)
    message_json.attachments = populate_attachments(message.attachments)
    if message.api_template is not None:
        message_json.api_template = str(message.api_template)

    if message.reply_to_email_address:
        message_json.reply_to_email_address = email_address_to_address_json(message.reply_to_email_address)

    return message_json


class InjectionRequestFactory(object):
    """
    Used by the Send function of the SocketLabsClient to generate an InjectionRequest for the Injection Api.
    """

    def __init__(self, server_id: int, api_key: str):
        """
        Creates a new instance of the InjectionRequestFactory.
        :param server_id: Your SocketLabs ServerId number.
        :type server_id: str
        :param api_key: Your SocketLabs Injection API key.
        :type api_key: str
        """
        self._api_key = api_key
        self._server_id = server_id

    def generate_request(self, message):
        """
        Generate the InjectionRequest for sending to the Injection Api.
        :param message: the message object to convert. BasicMessage and BulkMessage allowed
        :type message: BasicMessage, BulkMessage
        :return the converted InjectionRequest
        :rtype InjectionRequest
        """
        if isinstance(message, BasicMessage):
            return self.__generate_basic_message_request(message)
        elif isinstance(message, BulkMessage):
            return self.__generate_bulk_message_request(message)
        else:
            raise Exception('Message type was not BasicMessage, BulkMessage. No request can be generated')

    def __generate_bulk_message_request(self, message: BulkMessage):
        """
        Generate the InjectionRequest for sending to the Injection Api.
        :param message: the bulk message object to convert
        :type message: BulkMessage
        :return the converted InjectionRequest
        :rtype InjectionRequest
        """
        messageJson = generate_base_message(message)

        messageJson.to_email_address.append(AddressJson("%%DeliveryAddress%%", "%%RecipientName%%"))
        messageJson.merge_data = populate_merge_data(message.global_merge_data, message.to_recipient)

        request = InjectionRequest(self._server_id, self._api_key, [messageJson])

        return request

    def __generate_basic_message_request(self, message: BasicMessage):
        """
        Generate the InjectionRequest for sending to the Injection Api.
        :param message: the basic message object to convert
        :type message: BasicMessage
        :return the converted InjectionRequest
        :rtype InjectionRequest
        """
        messages_json = []
        messageJson = generate_base_message(message)

        if len(message.to_email_address) > 0:
            messageJson.to_email_address = populate_email_list(message.to_email_address)
        if len(message.cc_email_address) > 0:
            messageJson.cc_email_address = populate_email_list(message.cc_email_address)
        if len(message.bcc_email_address) > 0:
            messageJson.bcc_email_address = populate_email_list(message.bcc_email_address)

        messages_json.append(messageJson)

        request = InjectionRequest(self._server_id, self._api_key, messages_json)

        return request
