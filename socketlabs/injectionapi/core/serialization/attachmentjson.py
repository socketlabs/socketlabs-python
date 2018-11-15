from .customheaderjson import CustomHeaderJson


class AttachmentJson(object):
    """
    Represents a message attachment in the form of a byte array.
    To be serialized into JSON string before sending to the Injection Api.
    """

    def __init__(self):
        """
        Initializes a new instance of the AttachmentJson class
        """
        self._name = None
        self._mime_type = None
        self._content = None
        self._content_id = None
        self._custom_headers = []

    @property
    def name(self):
        """
        Get the name of attachment
        :return the name
        :rtype str
        """
        return str(self._name)

    @name.setter
    def name(self, val: str):
        """
        Set the name of attachment
        :param val: the name
        :type val: str
        """
        self._name = val

    @property
    def mime_type(self):
        """
        Get the MIME type of the attachment.
        :return the mime type
        :rtype str
        """
        return str(self._mime_type)

    @mime_type.setter
    def mime_type(self, val: str):
        """
        Set the MIME type of the attachment.
        :param val: the mime type
        :type val: str
        """
        self._mime_type = val

    @property
    def content_id(self):
        """
        Get ContentId for an Attachment.
        :return the content id
        :rtype: str
        """
        return str(self._content_id)

    @content_id.setter
    def content_id(self, val: str):
        """
        Set ContentId for an Attachment.
        :param val: the content id
        :type val: str
        """
        self._content_id = val

    @property
    def content(self):
        """
        Get Content of an Attachment. The BASE64 encoded str.
        :return the BASE64 encoded string of content
        :rtype str
        """
        return str(self._content)

    @content.setter
    def content(self, val: str):
        """
        Set Content of an Attachment. The BASE64 encoded str.
        :param val: the BASE64 encoded string of content
        :type val: str
        """
        self._content = val

    @property
    def custom_headers(self):
        """
        Get the list of custom headers added to the attachment.
        :return list of CustomHeader
        :rtype list
        """
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, val: list):
        """
        Set the list of custom headers added to the attachment.
        :param val: list of CustomHeader
        :type val: list
        """
        self._custom_headers = []
        if val is not None:
            for item in val:
                if isinstance(item, CustomHeaderJson):
                    self._custom_headers.append(item)

    def to_json(self):
        """
        build json dict for AttachmentJson
        :return the json dictionary
        :rtype dict
        """
        json = {
            "name":  self._name,
            "content": self._content,
            "contentType": self._mime_type
        }
        if self._content_id is not None and self._content_id.strip() != '':
            json["contentId"] = self._content_id

        if len(self._custom_headers) > 0:
            e = []
            for a in self._custom_headers:
                e.append(a.to_json())
            json["customHeaders"] = e
        return json
