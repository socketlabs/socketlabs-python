from .stringextension import StringExtension
from ..addressresult import AddressResult
from ..message.basicmessage import BasicMessage
from ..message.bulkmessage import BulkMessage
from ..message.messagebase import MessageBase
from ..sendresponse import SendResponse
from ..sendresult import SendResult

maximumRecipientsPerMessage = 50
""" Maximum recipient threshold """


def validate_base_message(message: MessageBase):
    """
    Validate the required fields of a BasicMessage.
    Fields validated are Subject, From Address, Reply To (if set),
    Message Body, and Custom Headers (if set)
    :param message: message to validate
    :type message: MessageBase
    :return the result
    :rtype SendResult
    """
    if not has_subject(message):
        return SendResult.MessageValidationEmptySubject

    if not has_from_email_address(message):
        return SendResult.EmailAddressValidationMissingFrom

    if not message.from_email_address.isvalid():
        return SendResult.EmailAddressValidationInvalidFrom

    if not has_valid_reply_to_email_address(message):
        return SendResult.RecipientValidationInvalidReplyTo

    if not has_message_body(message):
        return SendResult.MessageValidationEmptyMessage

    if message.custom_headers is not None and len(message.custom_headers) > 0:
        if not has_valid_custom_headers(message.custom_headers):
            return SendResult.MessageValidationInvalidCustomHeaders

    return SendResult.Success


def has_subject(message: MessageBase):
    """
    Check if the message has a subject
    :param message: message to validate
    :type message: MessageBase
    :return the result
    :rtype bool
    """
    return not StringExtension.is_none_or_white_space(message.subject)


def has_message_body(message: MessageBase):
    """
    Check if the message has a Message Body.
    If an Api Template is specified it will override the HtmlBody, AmpBody, and/or the textBody.
    If no Api Template is specified the HtmlBody, AmpBody, and/or the textBody must be set
    :param message: message to validate
    :type message: MessageBase
    :return the result
    :rtype bool
    """
    if has_api_template(message):
        return True

    hasHtmlBody = not StringExtension.is_none_or_white_space(message.html_body)
    hasPlainTextBody = not StringExtension.is_none_or_white_space(message.plain_text_body)

    return hasHtmlBody or hasPlainTextBody


def has_api_template(message: MessageBase):
    """
    Check if an ApiTemplate was specified and is valid
    :param message: message to validate
    :type message: MessageBase
    :return the result
    :rtype bool
    """
    if message.api_template and message.api_template > 0:
        return True
    return False


def has_from_email_address(message: MessageBase):
    """
    Check if the message has a valid From Email Address
    :param message: message to validate
    :type message: MessageBase
    :return the result
    :rtype bool
    """
    if not message.from_email_address:
        return False
    return not StringExtension.is_none_or_white_space(message.from_email_address.email_address)


def has_valid_reply_to_email_address(message: MessageBase):
    """
    Check if an ApiTemplate was specified and is valid
    :param message: message to validate
    :type message: MessageBase
    :return the result
    :rtype bool
    """
    if message.reply_to_email_address is None:
            return True

    hasEmailAddress = isinstance(message.reply_to_email_address.email_address, str) and \
        StringExtension.is_none_or_white_space(message.reply_to_email_address.email_address)
    hasFriendlyName = isinstance(message.reply_to_email_address.friendly_name, str) and \
        StringExtension.is_none_or_white_space(message.reply_to_email_address.friendly_name)

    if hasEmailAddress and hasFriendlyName:
        return True
    return message.reply_to_email_address.isvalid()


def validate_email_addresses(message: BasicMessage):
    """
    Validate email recipients for a basic message
    Checks the To, Cc, and the Bcc EmailAddress lists for the following:
        > At least 1 recipient is in the list.
        > Cumulative count of recipients in all 3 lists do not exceed the MaximumRecipientsPerMessage
        > Recipients in lists are valid.
    If errors are found, the SendResponse will contain the invalid email addresses
    :param message: message to validate
    :type message: BasicMessage
    :return the result
    :rtype SendResponse
    """
    recp_count = get_full_recipient_count(message)
    if recp_count <= 0:
        return SendResponse(SendResult.RecipientValidationNoneInMessage)
    if recp_count > maximumRecipientsPerMessage:
        return SendResponse(SendResult.RecipientValidationMaxExceeded)
    invalidRec = has_invalid_email_addresses(message)
    if invalidRec is not None and len(invalidRec) > 0:
        return SendResponse(SendResult.RecipientValidationInvalidRecipients, invalidRec)
    return SendResponse(SendResult.Success)


def validate_recipients(message: BulkMessage):
    """
    Validate email recipients for a bulk message
    Checks the To recipient lists for the following:
        > At least 1 recipient is in the list.
        > Cumulative count of recipients in all 3 lists do not exceed the MaximumRecipientsPerMessage
        > Recipients in lists are valid.
    If errors are found, the SendResponse will contain the invalid email addresses
    :param message: message to validate
    :type message: BulkMessage
    :return the result
    :rtype SendResponse
    """
    if message.to_recipient is None or len(message.to_recipient) <= 0:
        return SendResponse(SendResult.RecipientValidationMissingTo)
    if len(message.to_recipient) > maximumRecipientsPerMessage:
        return SendResponse(SendResult.RecipientValidationMaxExceeded)
    invalidRec = has_invalid_recipients(message)
    if invalidRec is not None and len(invalidRec) > 0:
        return SendResponse(SendResult.RecipientValidationInvalidRecipients, invalidRec)
    return SendResponse(SendResult.Success)


def has_invalid_email_addresses(message: BasicMessage):
    """
    Check all 3 EmailAddress lists To, Cc, and Bcc for valid email addresses
    :param message: message to validate
    :type message: BasicMessage
    :return list of invalid email as list of AddressResult
    :rtype list
    """
    invalid = []

    invalidTo = find_invalid_email_addresses(message.to_email_address)
    if invalidTo is not None and len(invalidTo) > 0:
        invalid.extend(invalidTo)

    invalidCc = find_invalid_email_addresses(message.cc_email_address)
    if invalidCc is not None and len(invalidCc) > 0:
        invalid.extend(invalidCc)

    invalidBcc = find_invalid_email_addresses(message.bcc_email_address)
    if invalidBcc is not None and len(invalidBcc) > 0:
        invalid.extend(invalidBcc)

    if len(invalid) > 0:
        return invalid
    else:
        return None


def has_invalid_recipients(message: BulkMessage):
    """
    Check the To recipient list for valid email addresses
    :param message: message to validate
    :type message: BulkMessage
    :return list of invalid email as list of AddressResult
    :rtype list
    """
    invalid = []

    invalidTo = find_invalid_recipients(message.to_recipient)
    if invalidTo is not None and len(invalidTo) > 0:
        invalid.extend(invalidTo)

    if len(invalid) > 0:
        return invalid
    else:
        return None


def find_invalid_email_addresses(email_addresses: list):
    """
    Check the list of EmailAddress for valid email addresses
    :param email_addresses: list of EmailAddress to validate
    :type email_addresses: list
    :return list of invalid email as list of AddressResult
    :rtype list
    """
    invalid = []
    if email_addresses is None:
        return None
    for item in email_addresses:
        if item.isvalid() is False:
            invalid.append(AddressResult(item.email_address, False, "InvalidAddress"))
    if len(invalid) > 0:
        return invalid
    else:
        return None


def find_invalid_recipients(recipients: list):
    """
    Check the list of BulkRecipient for valid email addresses
    :param recipients: list of BulkRecipient to validate
    :type recipients: list
    :return list of invalid email as list of AddressResult
    :rtype list
    """
    invalid = []
    if recipients is None:
        return None
    for item in recipients:
        valid = item.isvalid()
        if valid is False:
            invalid.append(AddressResult(item.email_address, False, "InvalidAddress"))
    if len(invalid) > 0:
        return invalid
    else:
        return None


def get_full_recipient_count(message: BasicMessage):
    """
    Cumulative count of email addresses in all 3 EmailAddress lists To, Cc, and Bcc
    :param message: message to count
    :type message: BasicMessage
    :return count of email addresses
    :rtype int
    """
    recipientCount = 0

    if message.to_email_address is not None:
        recipientCount += len(message.to_email_address)

    if message.cc_email_address is not None:
        recipientCount += len(message.cc_email_address)

    if message.bcc_email_address is not None:
        recipientCount += len(message.bcc_email_address)

    return recipientCount


def has_valid_custom_headers(custom_headers: list):
    """
    Check if the list of custom header is valid
    :param custom_headers: list of CustomHeader to validate
    :type custom_headers: list
    :return the result
     :rtype bool
    """
    if custom_headers is None:
        return True
    for item in custom_headers:
        valid = item.isvalid()
        if valid is False:
            return False
    return True


def validate_basic_message(message: BasicMessage):
    """
    Validate a basic email message before sending to the Injection API.
    :param message: message to validate
    :type message: BasicMessage
    :return the validation result
    :rtype SendResponse
    """
    valid_base = validate_base_message(message)
    if valid_base == SendResult.Success:
        return validate_email_addresses(message)

    return SendResponse(valid_base)


def validate_bulk_message(message: BulkMessage):
    """
    Validate a bulk email message before sending to the Injection API.
    :param message: message to validate
    :type message: BulkMessage
    :return the validation result
    :rtype SendResponse
    """
    valid_base = validate_base_message(message)
    if valid_base == SendResult.Success:
        return validate_recipients(message)

    return SendResponse(valid_base)


class SendValidator(object):
    """
    Used by the SocketLabsClient to conduct basic validation on the message before sending to the Injection API.
    """

    @staticmethod
    def validate_message(message):
        """
        Validate a basic email message before sending to the Injection API.
        :param message: message to validate
        :type message: BasicMessage
        :return the validation result
        :rtype SendResponse
        """

        if isinstance(message, BasicMessage):
            return validate_basic_message(message)

        if isinstance(message, BulkMessage):
            return validate_bulk_message(message)

    @staticmethod
    def validate_credentials(server_id: int, api_key: str):
        """
        Validate the ServerId and Api Key pair prior before sending to the Injection API.
        :param server_id: Your SocketLabs ServerId number.
        :type server_id: str
        :param api_key: Your SocketLabs Injection API key.
        :type api_key: str
        :return the validation result
        :rtype SendResponse
        """
        if api_key is None:
            return SendResponse(SendResult.AuthenticationValidationFailed)

        if server_id is None or server_id <= 0:
            return SendResponse(SendResult.AuthenticationValidationFailed)

        return SendResponse(SendResult.Success)
