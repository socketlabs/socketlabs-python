from ...addressresult import AddressResult


class MessageResultDto(object):
    """
    Data transfer object representing a message result from the Injection Api.
    """

    def __init__(self):
        """
        Create an instance of the MessageResultDto class
        """
        self._index = None
        self._error_code = None
        self._address_results = None

    @property
    def index(self):
        """
        Get the index of message being sent
        :return the index
        :rtype int
        """
        return self._index

    @index.setter
    def index(self, val: int):
        """
        Set the index of message being sent
        :param val: the index
        :type val: str
        """
        self._index = val

    @property
    def error_code(self):
        """
        Get the response ErrorCode
        :return the error code
        :rtype str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, val: str):
        """
        Set the response ErrorCode
        :param val: the error code
        :type val: str
        """
        self._error_code = val

    @property
    def address_results(self):
        """
        Get the List of AddressResult objects
        :return the list of AddressResult
        :rtype list
        """
        return self._address_results

    @address_results.setter
    def address_results(self, val: list):
        """
        Set the List of AddressResult objects
        :param val: the list of AddressResult
        :type val: list
        """
        self._address_results = []
        if val is not None:
            for item in val:
                if isinstance(item, AddressResult):
                    self._address_results.append(item)

    def to_json(self):
        """
        build json dict for MessageResultDto
        :return the json dictionary
        :rtype dict
        """
        json = {
            "ErrorCode": self._error_code,
            "Index": self._index
        }
        if len(self._address_results) > 0:
            e = []
            for a in self._address_results:
                e.append(a.to_json())
            json["AddressResult"] = e
        return json
