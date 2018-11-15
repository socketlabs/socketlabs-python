import unittest

from socketlabs.injectionapi.message.customheader import CustomHeader

from socketlabs.injectionapi.message.bulkrecipient import BulkRecipient

from socketlabs.injectionapi.core.sendvalidator import *
from socketlabs.injectionapi.message.basicmessage import BasicMessage
from socketlabs.injectionapi.message.emailaddress import EmailAddress
from tests.random_helper import RandomHelper


class TestSendValidator(unittest.TestCase):
    """
    Testing the SendValidator
    """

    def setUp(self):
        self.random_helper = RandomHelper()
        pass

    """ validate_base_message """

    def test_validate_base_message_ReturnsMessageValidationEmptySubject_WhenSubjectIsEmpty(self):
        
        #  Arrange
        message = BasicMessage()
        message.subject = None

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.MessageValidationEmptySubject, actual)

    def test_validate_base_message_ReturnsEmailAddressValidationMissingFrom_WhenFromRecipientIsNone(self):
        
        #  Arrange
        message = BasicMessage()
        message.subject = self.random_helper.random_string()
        message.from_email_address = None

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.EmailAddressValidationMissingFrom, actual)

    def test_validate_base_message_ReturnsEmailAddressValidationMissingFrom_WhenFromRecipientIsObjWithNone(self):

        #  Arrange
        message = BasicMessage()
        message.subject = self.random_helper.random_string()
        message.from_email_address = EmailAddress(None)

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.EmailAddressValidationMissingFrom, actual)

    def test_validate_base_message_ReturnsEmailAddressValidationMissingFrom_WhenFromRecipientIsEmpty(self):
        #  Arrange
        message = BasicMessage()
        message.subject = self.random_helper.random_string()
        message.from_email_address = EmailAddress('')

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.EmailAddressValidationMissingFrom, actual)

    def test_validate_base_message_ReturnsEmailAddressValidationInvalidFrom_WhenFromRecipientIsInvalid(self):
        #  Arrange
        message = BasicMessage()
        message.subject = self.random_helper.random_string()
        message.from_email_address = EmailAddress("$$##%%")

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.EmailAddressValidationInvalidFrom, actual)

    def test_validate_base_message_ReturnsMessageValidationEmptyMessage_WhenAllBodyFieldsAreEmpty(self):
        #  Arrange
        message = BasicMessage()
        message.subject = self.random_helper.random_string()
        message.from_email_address = self.random_helper.random_email_address()
        message.html_body = None
        message.plain_text_body = None
        message.api_template = None

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.MessageValidationEmptyMessage, actual)

    def test_validate_base_message_ReturnsMessageValidationInvalidCustomHeaders_WhenCustomHeadersAreInvalid(self):
        #  Arrange
        message = BasicMessage()
        message.subject = self.random_helper.random_string()
        message.from_email_address = self.random_helper.random_email_address()
        message.html_body = self.random_helper.random_string()
        message.add_custom_header("", "")

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.MessageValidationInvalidCustomHeaders, actual)

    def test_validate_base_message_ReturnsSuccess_WhenSubjectAndFromRecipientAndHtmlBodyIsNotEmpty(self):
        #  Arrange
        message = BasicMessage()
        message.subject = self.random_helper.random_string()
        message.from_email_address = self.random_helper.random_email_address()
        message.html_body = self.random_helper.random_string()

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.Success, actual)

    def test_validate_base_message_ReturnsSuccess_WhenSubjectAndFromRecipientAndPlainTextBodyIsNotEmpty(self):
        #  Arrange
        message = BasicMessage()
        message.subject = self.random_helper.random_string()
        message.from_email_address = self.random_helper.random_email_address()
        message.plain_text_body = self.random_helper.random_string()

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.Success, actual)

    def test_validate_base_message_ReturnsSuccess_WhenSubjectAndFromRecipientAndApiTemplateIsNotEmpty(self):
        #  Arrange
        message = BasicMessage()
        message.subject = self.random_helper.random_string()
        message.from_email_address = self.random_helper.random_email_address()
        message.api_template = self.random_helper.random_int()

        #  Act
        actual = validate_base_message(message)

        #  Assert
        self.assertEqual(SendResult.Success, actual)

    """ has_message_body """

    def test_has_message_body_ReturnsFalse_WhenHtmlBodyAndPlainTextBodyAndApiTemplateIsEmpty(self):
        # Arrange
        message = BasicMessage()
        message.html_body = None
        message.plain_text_body = None
        message.api_template = None

        # Act
        actual = has_message_body(message)

        # Assert
        self.assertFalse(actual)

    def test_has_message_body_ReturnsTrue_WhenHtmlBodyAndApiTemplateIsEmptyAndPlainTextBodyIsNotEmpty(self):
        # Arrange
        message = BasicMessage()
        message.html_body = None
        message.plain_text_body = self.random_helper.random_string()
        message.api_template = None

        # Act
        actual = has_message_body(message)

        # Assert
        self.assertTrue(actual)

    def test_has_message_body_ReturnsTrue_WhenPlainTextBodyAndApiTemplateIsNotEmptyAndHtmlBodyIsEmpty(self):
        # Arrange
        message = BasicMessage()
        message.html_body = self.random_helper.random_string()
        message.plain_text_body = None
        message.api_template = None

        # Act
        actual = has_message_body(message)

        # Assert
        self.assertTrue(actual)

    def test_has_message_body_ReturnsTrue_WhenApiTemplateIsNotEmptyAndPlainTextBodyAndHtmlBodyIsEmpty(self):
        # Arrange
        message = BasicMessage()
        message.html_body = None
        message.plain_text_body = None
        message.api_template = self.random_helper.random_int()

        # Act
        actual = has_message_body(message)

        # Assert
        self.assertTrue(actual)

    """ has_api_template """

    def test_has_api_template_ReturnsTrue_WhenApiTemplateIsNotZero(self):
        # Arrange
        message = BasicMessage()
        message.api_template = self.random_helper.random_int(1, 10)

        # Act
        actual = has_api_template(message)

        # Assert
        self.assertTrue(actual)

    def test_has_api_template_ReturnsTrue_WhenApiTemplateIsNotMinValue(self):
        # Arrange
        message = BasicMessage()
        message.api_template = self.random_helper.random_int(1, 10)

        # Act
        actual = has_api_template(message)

        # Assert
        self.assertTrue(actual)

    def test_has_api_template_ReturnsFalse_WhenApiTemplateIsZero(self):
        # Arrange
        message = BasicMessage()
        message.api_template = 0

        # Act
        actual = has_api_template(message)

        # Assert
        self.assertFalse(actual)

    def test_has_api_template_ReturnsFalse_WhenApiTemplateIsLessThanZero(self):
        # Arrange
        message = BasicMessage()
        message.api_template = -1

        # Act
        actual = has_api_template(message)

        # Assert
        self.assertFalse(actual)

    """ validate_email_addresses (BasicMessage) """
        
    def test_validate_email_addresses_BasicMessage_ReturnsNoRecipients_WhenToAndCcAndBccIsNone(self):
        #  Arrange
        message = BasicMessage()

        #  Act
        actual = validate_email_addresses(message)

        #  Assert
        self.assertEqual(SendResult.RecipientValidationNoneInMessage, actual.result)
        
    def test_validate_email_addresses_BasicMessage_ReturnsSuccess_WhenToIsNotEmpty(self):
        #  Arrange
        message = BasicMessage()
        message.to_email_address = [self.random_helper.random_email_address()]

        #  Act
        actual = validate_email_addresses(message)

        #  Assert
        self.assertEqual(SendResult.Success, actual.result)
        
    def test_validate_email_addresses_BasicMessage_ReturnsSuccess_WhenCcIsNotEmpty(self):
        #  Arrange
        message = BasicMessage()
        message.cc_email_address = [self.random_helper.random_email_address()]

        #  Act
        actual = validate_email_addresses(message)

        #  Assert
        self.assertEqual(SendResult.Success, actual.result)
        
    def test_validate_email_addresses_BasicMessage_ReturnsSuccess_WhenBccIsNotEmpty(self):
        #  Arrange
        message = BasicMessage()
        message.bcc_email_address = [self.random_helper.random_email_address()]

        #  Act
        actual = validate_email_addresses(message)

        #  Assert
        self.assertEqual(SendResult.Success, actual.result)
        
    def test_validate_email_addresses_BasicMessage_ReturnsTooManyRecipients_WhenEmailListHasToManyRecipients(self):
        #  Arrange
        num_in_list = int(maximumRecipientsPerMessage / 2)
        message = BasicMessage()
        message.to_email_address = self.random_helper.random_list_of_email_addresses(num_in_list)
        message.cc_email_address = self.random_helper.random_list_of_email_addresses(num_in_list)
        message.bcc_email_address = self.random_helper.random_list_of_email_addresses(num_in_list)

        #  Act
        actual = validate_email_addresses(message)

        #  Assert
        self.assertEqual(SendResult.RecipientValidationMaxExceeded, actual.result)
        
    def test_validate_email_addresses_BasicMessage_ReturnsTooManyRecipients_WhenToHasToManyRecipients(self):
        #  Arrange
        num_in_list = int(maximumRecipientsPerMessage + 1)
        message = BasicMessage()
        message.to_email_address = self.random_helper.random_list_of_email_addresses(num_in_list)

        #  Act
        actual = validate_email_addresses(message)

        #  Assert
        self.assertEqual(SendResult.RecipientValidationMaxExceeded, actual.result)

    """ validate_recipients (BulkMessage) """

    def test_validate_recipients_BulkMessage_ReturnsNoRecipients_WhenToIsNone(self):
        # Arrange
        message = BulkMessage()
        message.to_recipient = None

        # Act
        actual = validate_recipients(message)

        # Assert
        self.assertEqual(SendResult.RecipientValidationMissingTo, actual.result)

    def test_validate_recipients_BulkMessage_ReturnsNoRecipients_WhenToIsEmpty(self):
        # Arrange
        message = BulkMessage()
        message.to_recipient = []

        # Act
        actual = validate_recipients(message)

        #  Assert
        self.assertEqual(SendResult.RecipientValidationMissingTo, actual.result)

    def test_validate_recipients_BulkMessage_ReturnsTooManyRecipients_WhenToHasToManyRecipients(self):
        # Arrange
        num_in_list = maximumRecipientsPerMessage + 1
        message = BulkMessage()
        message.to_recipient = self.random_helper.random_list_of_bulk_recipients(num_in_list)

        # Act
        actual = validate_recipients(message)

        #  Assert
        self.assertEqual(SendResult.RecipientValidationMaxExceeded, actual.result)

    """ has_subject """
    
    def test_has_subject_ReturnsFalse_WhenSubjectIsEmpty(self):
        message = BasicMessage()
        message.subject = None

        actual = has_subject(message)

        self.assertFalse(actual)

    def test_has_subject_ReturnsTrue_WhenSubjectIsNotEmpty(self):
        message = BasicMessage()
        message.subject = self.random_helper.random_string()

        actual = has_subject(message)

        self.assertTrue(actual)

    """ has_from_email_address """

    def test_has_from_email_address_ReturnsFalse_WhenFromEmailIsNone(self):
        # Arrange
        message = BasicMessage()
        message.from_email_address = None

        # Act
        actual = has_from_email_address(message)

        # Assert
        self.assertFalse(actual)

    def test_has_from_email_address_ReturnsFalse_WhenFromEmailIsInvalid(self):
        # Arrange
        message = BasicMessage()
        message.from_email_address = EmailAddress(None)

        # Act
        actual = has_from_email_address(message)

        # Assert
        self.assertFalse(actual)

    def test_has_from_email_address_ReturnsFalse_WhenFromEmailIsEmpty(self):
        # Arrange
        message = BasicMessage()
        message.from_email_address = EmailAddress('')

        # Act
        actual = has_from_email_address(message)

        # Assert
        self.assertFalse(actual)

    def test_has_from_email_address_ReturnsTrue_WhenFromEmailIsNotEmpty(self):
        # Arrange
        message = BasicMessage()
        message.from_email_address = self.random_helper.random_email_address()

        # Act
        actual = has_from_email_address(message)

        # Assert
        self.assertTrue(actual)

    """ has_valid_reply_to_email_address """

    def test_has_valid_reply_to_email_address_ReturnsTrue_WhenReplyToEmailIsNone(self):
        # Arrange
        message = BasicMessage()
        message.reply_to_email_address = None

        # Act
        actual = has_valid_reply_to_email_address(message)

        # Assert
        self.assertTrue(actual)

    def test_has_valid_reply_to_email_address_ReturnsFalse_WhenReplyToEmailIsInvalid(self):
        # Arrange
        message = BasicMessage()
        message.reply_to_email_address = EmailAddress(None)

        # Act
        actual = has_valid_reply_to_email_address(message)

        # Assert
        self.assertFalse(actual)

    def test_has_valid_reply_to_email_address_ReturnsFalse_WhenReplyToEmailIsEmpty(self):
        # Arrange
        message = BasicMessage()
        message.reply_to_email_address = EmailAddress('')

        # Act
        actual = has_valid_reply_to_email_address(message)

        # Assert
        self.assertFalse(actual)

    def test_has_valid_reply_to_email_address_ReturnsTrue_WhenReplyToEmailIsNotEmpty(self):
        # Arrange
        message = BasicMessage()
        message.reply_to_email_address = self.random_helper.random_email_address()

        # Act
        actual = has_valid_reply_to_email_address(message)

        # Assert
        self.assertTrue(actual)

    """ get_full_recipient_count """

    def test_get_full_recipient_count_BasicMessage_ReturnsGT0_WhenOnlyToRecipientsHasOneValue(self):
        # Arrange
        message = BasicMessage()
        message.to_email_address = self.random_helper.random_list_of_email_addresses(1)

        # Act
        actual = get_full_recipient_count(message)

        # Assert
        self.assertTrue(actual > 0)

    def test_get_full_recipient_count_BasicMessage_ReturnsGT0_WhenOnlyCcRecipientsHasOneValue(self):
        # Arrange
        message = BasicMessage()
        message.cc_email_address = self.random_helper.random_list_of_email_addresses(1)

        # Act
        actual = get_full_recipient_count(message)

        # Assert
        self.assertTrue(actual > 0)

    def test_get_full_recipient_count_BasicMessage_ReturnsGT0_WhenOnlyBccRecipientsHasOneValue(self):
        # Arrange
        message = BasicMessage()
        message.bcc_email_address = self.random_helper.random_list_of_email_addresses(1)

        # Act
        actual = get_full_recipient_count(message)

        # Assert
        self.assertTrue(actual > 0)

    def test_get_full_recipient_count_BasicMessage_Returns3_WhenEachRecipientsHasValue(self):
        # Arrange
        message = BasicMessage()
        message.to_email_address = self.random_helper.random_list_of_email_addresses(1)
        message.cc_email_address = self.random_helper.random_list_of_email_addresses(1)
        message.bcc_email_address = self.random_helper.random_list_of_email_addresses(1)

        # Act
        actual = get_full_recipient_count(message)

        # Assert
        self.assertTrue(actual > 0)

    def test_get_full_recipient_count_BasicMessage_Returns0_WhenNoRecipientsAdded(self):
        # Arrange
        message = BasicMessage()

        # Act
        actual = get_full_recipient_count(message)

        # Assert
        self.assertEqual(0, actual)

    """ has_invalid_email_addresses (BasicMessage) """

    def test_has_invalid_email_addresses_BasicMessage_ReturnsListOfOne_WhenToHasOneInvalid(self):
        # Arrange
        message = BasicMessage()
        message.to_email_address = [EmailAddress(self.random_helper.random_string())]
        
        # Act        
        actual = has_invalid_email_addresses(message)

        # Assert
        self.assertEqual(1, len(actual))

    def test_has_invalid_email_addresses_BasicMessage_ReturnsListOfOne_WhenCcHasOneInvalid(self):
        # Arrange
        message = BasicMessage()
        message.cc_email_address = [EmailAddress(self.random_helper.random_string())]

        # Act
        actual = has_invalid_email_addresses(message)

        # Assert
        self.assertEqual(1, len(actual))

    def test_has_invalid_email_addresses_BasicMessage_ReturnsListOfOne_WhenBccHasOneInvalid(self):
        # Arrange
        message = BasicMessage()
        message.bcc_email_address = [EmailAddress(self.random_helper.random_string())]

        # Act
        actual = has_invalid_email_addresses(message)

        # Assert
        self.assertEqual(1, len(actual))

    def test_has_invalid_email_addresses_BasicMessage_ReturnsListOfThree_WhenEachRecipientHasOneInvalid(self):
        # Arrange
        message = BasicMessage()
        message.to_email_address = [EmailAddress(self.random_helper.random_string())]
        message.cc_email_address = [EmailAddress(self.random_helper.random_string())]
        message.bcc_email_address = [EmailAddress(self.random_helper.random_string())]

        # Act
        actual = has_invalid_email_addresses(message)

        # Assert
        self.assertEqual(3, len(actual))

    def test_has_invalid_email_addresses_BasicMessage_ReturnsNull_WhenNoInvalidRecipientsFound(self):
        # Arrange
        message = BasicMessage()
        message.to_email_address = self.random_helper.random_list_of_email_addresses(1)
        message.cc_email_address = self.random_helper.random_list_of_email_addresses(1)
        message.bcc_email_address = self.random_helper.random_list_of_email_addresses(1)

        # Act
        actual = has_invalid_email_addresses(message)

        # Assert
        self.assertIsNone(actual)

    """ has_invalid_recipients(BulkMessage) """

    def test_has_invalid_recipients_BulkMessage_ReturnsListOfOne_WhenToHasOneInvalid(self):
        
        # Arrange
        message = BulkMessage()
        message.to_recipient = [BulkRecipient(self.random_helper.random_string())]

        # Act
        actual = has_invalid_recipients(message)

        # Assert
        self.assertEqual(1, len(actual))

    def test_has_invalid_recipients_BasicMessage_ReturnsListOfThree_WhenToHasThreeInvalid(self):
        
        # Arrange
        message = BulkMessage()
        message.to_recipient = [
            BulkRecipient(self.random_helper.random_string()),
            BulkRecipient(self.random_helper.random_string()),
            BulkRecipient(self.random_helper.random_string())
        ]

        # Act
        actual = has_invalid_recipients(message)

        # Assert
        self.assertEqual(3, len(actual))

    def test_has_invalid_recipients_BulkMessage_ReturnsNull_WhenNoInvalidRecipientsFound(self):
        # Arrange
        message = BulkMessage()
        message.to_recipient = self.random_helper.random_list_of_bulk_recipients(3)

        # Act
        actual = has_invalid_recipients(message)

        # Assert
        self.assertIsNone(actual)

    """ find_invalid_email_addresses(list of EmailAddress) """

    def test_find_invalid_email_addresses_ListOfEmailAddress_ReturnsNull_WhenRecipientsIsNone(self):
        # Arrange
        addresses = None

        # Act
        # noinspection PyTypeChecker
        actual = find_invalid_email_addresses(addresses)

        # Assert
        self.assertIsNone(actual)

    def test_find_invalid_email_addresses_ListOfEmailAddress_ReturnsNull_WhenRecipientsIsEmpty(self):
        # Arrange
        addresses = []

        # Act
        actual = find_invalid_email_addresses(addresses)

        # Assert
        self.assertIsNone(actual)

    def test_find_invalid_email_addresses_ListOfEmailAddress_ReturnsNull_WhenNoInvalidRecipientsFound(self):
        # Arrange
        addresses = [self.random_helper.random_email_address()]

        # Act
        actual = find_invalid_email_addresses(addresses)

        # Assert
        self.assertIsNone(actual)

    def test_find_invalid_email_addresses_ListOfEmailAddress_ReturnsList_WhenInvalidRecipientsFound(self):
        # Arrange
        addresses = [EmailAddress(self.random_helper.random_string())]

        # Act
        actual = find_invalid_email_addresses(addresses)

        # Assert
        self.assertEqual(1, len(actual))

    """ find_invalid_recipients(BulkRecipient message) """

    def test_find_invalid_recipients_ListOfBulkRecipient_ReturnsNull_WhenRecipientsIsNone(self):
        # Arrange
        addresses = None

        # Act
        # noinspection PyTypeChecker
        actual = find_invalid_recipients(addresses)

        # Assert
        self.assertIsNone(actual)

    def test_find_invalid_recipients_ListOfBulkRecipient_ReturnsNull_WhenRecipientsIsEmpty(self):
        # Arrange
        addresses = []

        # Act
        actual = find_invalid_recipients(addresses)

        # Assert
        self.assertIsNone(actual)

    def test_find_invalid_recipients_ListOfBulkRecipient_ReturnsNull_WhenNoInvalidRecipientsFound(self):
        # Arrange
        addresses = self.random_helper.random_list_of_bulk_recipients(1)

        # Act
        actual = find_invalid_recipients(addresses)

        # Assert
        self.assertIsNone(actual)

    def test_find_invalid_recipients_ListOfBulkRecipient_ReturnsList_WhenInvalidRecipientsFound(self):
        # Arrange
        addresses = [BulkRecipient(self.random_helper.random_string())]

        # Act
        actual = find_invalid_recipients(addresses)

        # Assert
        self.assertEqual(1, len(actual))

    """ has_valid_custom_headers """

    def test_has_valid_custom_headers_ReturnsFalse_WhenKeyAndValueAreEmpty(self):
        # Arrange
        headers = [CustomHeader("", "")]

        # Act
        actual = has_valid_custom_headers(headers)

        # Assert
        self.assertFalse(actual)

    def test_has_valid_custom_headers_ReturnsFalse_WhenKeyIsNotEmptyAndValueIsEmpty(self):
        # Arrange
        headers = [CustomHeader(self.random_helper.random_string(), "")]

        # Act
        actual = has_valid_custom_headers(headers)

        # Assert
        self.assertFalse(actual)

    def test_has_valid_custom_headers_ReturnsFalse_WhenKeyIsEmptyAndValueIsNotEmpty(self):
        # Arrange
        headers = [CustomHeader("", self.random_helper.random_string())]

        # Act
        actual = has_valid_custom_headers(headers)

        # Assert
        self.assertFalse(actual)

    def test_has_valid_custom_headers_ReturnsTrue_WhenListIsNone(self):
        # Arrange
        headers = None

        # Act
        # noinspection PyTypeChecker
        actual = has_valid_custom_headers(headers)

        # Assert
        self.assertTrue(actual)

    def test_has_valid_custom_headers_ReturnsTrue_WhenListIsEmpty(self):
        # Arrange
        headers = []

        # Act
        actual = has_valid_custom_headers(headers)

        # Assert
        self.assertTrue(actual)

    def test_has_valid_custom_headers_ReturnsTrue_WhenListIsValid(self):
        # Arrange
        headers = [CustomHeader(self.random_helper.random_string(), self.random_helper.random_string())]
        
        # Act
        actual = has_valid_custom_headers(headers)

        # Assert
        self.assertTrue(actual)
        
    """ validate_credentials """

    def test_validate_credentials_ReturnsAuthenticationError_WhenServerIdAndApiKeyIsEmpty(self):
        # Arrange

        server_id = None
        api_key = None
        validator = SendValidator()

        # Act
        # noinspection PyTypeChecker
        actual = validator.validate_credentials(server_id, api_key)

        # Assert
        self.assertEqual(SendResult.AuthenticationValidationFailed, actual.result)

    def test_validate_credentials_ReturnsAuthenticationError_WhenServerIdIsNotEmptyAndApiKeyIsEmpty(self):
        # Arrange
        server_id = self.random_helper.random_server_id()
        api_key = None
        validator = SendValidator()

        # Act
        # noinspection PyTypeChecker
        actual = validator.validate_credentials(server_id, api_key)

        # Assert
        self.assertEqual(SendResult.AuthenticationValidationFailed, actual.result)
    
    def test_validate_credentials_ReturnsAuthenticationError_WhenApiKeyIsNotEmptyAndServerIdIsEmpty(self):
    
        # Arrange
        server_id = None
        api_key = self.random_helper.random_string()
        validator = SendValidator()

        # Act
        # noinspection PyTypeChecker
        actual = validator.validate_credentials(server_id, api_key)

        # Assert
        self.assertEqual(SendResult.AuthenticationValidationFailed, actual.result)

    def test_validate_credentials_ReturnsSuccess_WhenApiKeyAndServerIdIsNotEmpty(self):
    
        # Arrange
        server_id = self.random_helper.random_server_id()
        api_key = self.random_helper.random_string()
        validator = SendValidator()

        # Act
        actual = validator.validate_credentials(server_id, api_key)

        # Assert
        self.assertEqual(SendResult.Success, actual.result)
        

if __name__ == '__main__':
    unittest.main()
