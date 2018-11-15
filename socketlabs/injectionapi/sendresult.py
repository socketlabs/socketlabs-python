from enum import Enum


class SendResult(Enum):        
    """ 
    Enumerated result of the client send 
    """

    """ An error has occurred that was unforeseen """
    UnknownError = 0

    """ A timeout occurred sending the message """
    Timeout = 1

    """ Successful send of message """
    Success = 2

    """ Warnings were found while sending the message """
    Warning = 3

    """ Internal server error """
    InternalError = 4

    """ Message size has exceeded the size limit """
    MessageTooLarge = 5

    """ Message exceeded maximum recipient count in the message """
    TooManyRecipients = 6

    """ Invalid data was found on the message """
    InvalidData = 7

    """ The account is over the send quota, rate limit exceeded """
    OverQuota = 8

    """ Too many errors occurred sending the message """
    TooManyErrors = 9

    """ The ServerId/ApiKey combination is invalid """
    InvalidAuthentication = 10

    """ The account has been disabled """
    AccountDisabled = 11

    """ Too many messages were found in the request """
    TooManyMessages = 12

    """ No valid recipients were found in the message """
    NoValidRecipients = 13

    """ An invalid recipient were found on the message """
    InvalidAddress = 14

    """ An invalid attachment were found on the message """
    InvalidAttachment = 15

    """ No message was found in the request """
    NoMessages = 16

    """ No message body was found in the message """
    EmptyMessage = 17

    """ No subject was found in the message """
    EmptySubject = 18

    """ An invalid from address was found on the message """
    InvalidFrom = 19

    """ No To addresses were found in the message """
    EmptyToAddress = 20

    """ No valid message body was found in the message """
    NoValidBodyParts = 21

    """ An invalid TemplateId was found in the message """
    InvalidTemplateId = 22

    """ The specified TemplateId has no content for the message """
    TemplateHasNoContent = 23

    """ A conflict occurred on the message body of the message """
    MessageBodyConflict = 24

    """ Invalid MergeData was found on the message """
    InvalidMergeData = 25

    """ SDK Validation Error : Authentication Validation Failed, Missing or invalid ServerId or ApiKey """
    AuthenticationValidationFailed = 26

    """ SDK Validation Error : From email address is missing in the message """
    EmailAddressValidationMissingFrom = 27

    """ SDK Validation Error : From email address in the message is invalid """
    EmailAddressValidationInvalidFrom = 28

    """ SDK Validation Error : Message exceeded maximum recipient count in the message """
    RecipientValidationMaxExceeded = 29

    """ SDK Validation Error : No Recipients were found in the message """
    RecipientValidationNoneInMessage = 30

    """ SDK Validation Error : To addresses are missing in the message """
    RecipientValidationMissingTo = 31

    """ SDK Validation Error : Invalid ReplyTo Address was found in the message """
    RecipientValidationInvalidReplyTo = 32

    """ SDK Validation Error : Invalid recipients were found in the message """
    RecipientValidationInvalidRecipients = 33

    """ SDK Validation Error : No Subject was found in the message """
    MessageValidationEmptySubject = 34

    """ SDK Validation Error : No message body was found in the message """
    MessageValidationEmptyMessage = 35

    """ SDK Validation Error : Invalid Custom Headers were found in the message """
    MessageValidationInvalidCustomHeaders = 36

    def __str__(self):
        """
        String representation of the SendResult Enum
        :return the string
        :rtype str
        """
        switcher = {
            0: "An error has occurred that was unforeseen",
            1: "A timeout occurred sending the message",
            2: "Successful send of message",
            3: "Warnings were found while sending the message",
            4: "Internal server error",
            5: "Message size has exceeded the size limit",
            6: "Message exceeded maximum recipient count in the message",
            7: "Invalid data was found on the message",
            8: "The account is over the send quota, rate limit exceeded",
            9: "Too many errors occurred sending the message",
            10: "The ServerId/ApiKey combination is invalid",
            11: "The account has been disabled",
            12: "Too many messages were found in the request",
            13: "No valid recipients were found in the message",
            14: "An invalid recipient were found on the message",
            15: "An invalid attachment were found on the message",
            16: "No message body was found in the message",
            17: "No message body was found in the message",
            18: "No subject was found in the message",
            19: "An invalid from address was found on the message",
            20: "No To addresses were found in the message",
            21: "No valid message body was found in the message",
            22: "An invalid TemplateId was found in the message",
            23: "The specified TemplateId has no content for the message",
            24: "A conflict occurred on the message body of the message",
            25: "Invalid MergeData was found on the message",
            26: "SDK Validation Error : "
                "Authentication Validation Failed, Missing or invalid ServerId or ApiKey",
            27: "SDK Validation Error : "
                "From email address is missing in the message",
            28: "SDK Validation Error : "
                "From email address in the message is invalid",
            29: "SDK Validation Error : "
                "Message exceeded maximum recipient count in the message",
            30: "SDK Validation Error : No Recipients were found in the message",
            31: "SDK Validation Error : To addresses are missing in the message",
            32: "SDK Validation Error : "
                "Invalid ReplyTo Address was found in the message",
            33: "SDK Validation Error : Invalid recipients were found in the message",
            34: "SDK Validation Error : No Subject was found in the message",
            35: "SDK Validation Error : No message body was found in the message",
            36: "SDK Validation Error : "
                "Invalid Custom Headers were found in the message",
        }
        return switcher.get(self.value, "An error has occurred that was unforeseen")

    def describe(self):
        """
        string output of the
        :return the string
        :rtype str
        """
        return self.name, self.value, self.__str__
