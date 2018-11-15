# serialization
from .messageresultdto import MessageResultDto


class InjectionResponseDto(object):
    """
    Represents an individual email address for a message.
    To be serialized into JSON string before sending to the Injection Api.
    """

    def __init__(self):
        """
        Initializes a new instance of the AddressJson class
        """
        self._error_code = None
        self._transaction_receipt = None
        self._message_results = None

    @property
    def error_code(self):
        """
        Get the response ErrorCode of the Injection Api send request
        :return the response error code
        :rtype string
        """
        return self._error_code

    @error_code.setter
    def error_code(self, val: str):
        """
        Set the response ErrorCode of the Injection Api send request
        :param val: the response error code
        :type val: str
        """
        self._error_code = val

    @property
    def transaction_receipt(self):
        """
        Get the transaction receipt of the Injection Api send request
        :return the transaction receipt
        :rtype str
        """
        return self._transaction_receipt

    @transaction_receipt.setter
    def transaction_receipt(self, val: str):
        """
        Set the transaction receipt of the Injection Api send request
        :param val: the transaction receipt
        :type val: str
        """
        self._transaction_receipt = val

    @property
    def message_results(self):
        """
        Get the array of MessageResultDto objects that contain the status of each message sent.
        :return the list MessageResultDto
        :rtype list
        """
        return self._message_results

    @message_results.setter
    def message_results(self, val: list):
        """
        Set the array of MessageResultDto objects that contain the status of each message sent.
        :param val: the list MessageResultDto
        :type val: list
        """
        self._message_results = []
        if val is not None:
            for item in val:
                if isinstance(item, MessageResultDto):
                    self._message_results.append(item)

    def to_json(self):
        """
        build json dict for InjectionResponseDto
        :return the json dictionary
        :rtype dict
        """
        json = {
            "errorCode": self._error_code,
            "transactionReceipt": self._transaction_receipt
        }
        if len(self._message_results) > 0:
            e = []
            for a in self._message_results:
                e.append(a.to_json())
            json["messageResult"] = e
        return json
