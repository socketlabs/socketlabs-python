class MergeFieldJson(object):
    """
    Represents a merge field as a field and value pair.
    To be serialized into JSON string before sending to the Injection Api.
    """

    def __init__(self, field: str = None, val: str = None):
        """
        Initializes a new instance of the MergeFieldJson class
        :param field: the field of the merge field
        :type field: str
        :param val: the value of the merge field
        :type val: str
        """
        self._field = field
        self._value = val

    @property
    def field(self):
        """
        The field of your merge field.
        :return the field
        :rtype str
        """
        return str(self._field)

    @field.setter
    def field(self, val: str):
        """
        Set the field of your merge field.
        :param val: the field
        :type val: str
        """
        self._field = val

    @property
    def value(self):
        """
        The merge field value.
        :return the value
        :rtype str
        """
        return str(self._value)

    @value.setter
    def value(self, val: str):
        """
        Set the merge field value.
        :param val: the value
        :type val: str
        """
        self._value = val

    def to_json(self):
        """
        build json dict for MergeFieldJson
        :return the json dictionary
        :rtype dict
        """
        return {
            "field":  self._field,
            "value": self._value
        }
