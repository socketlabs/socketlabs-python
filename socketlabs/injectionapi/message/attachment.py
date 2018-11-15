import base64
import os
import mimetypes


from .customheader import CustomHeader


class Attachment(object):
    """
    Represents a message attachment in the form of a byte array.

    :Example:

         attachment1 = Attachment(file_path="./bus.png")

         attachment2 = Attachment("bus", "image/png", "../bus.png")

         attachment3 = Attachment("bus", "image/png", content=bytes())
         attachment3.add_custom_header("name1", "value1")
         attachment3.add_custom_header("name2", "value2")

    """

    def __init__(self, name: str = None, mime_type: str = None, file_path: str = None, content: bytes = None):
        """
        Initializes a new instance of the Attachment class
        :param name: the name
        :type name: str
        :param mime_type: the mime type
        :type mime_type: str
        :param file_path: the local file path
        :type file_path: str
        """
        self._name = None
        self._mime_type = None
        self._content = None
        self._content_id = None
        self._custom_headers = []

        if file_path is not None:
            self.readfile(file_path)

        if name is not None:
            self._name = name

        if mime_type is not None:
            self._mime_type = mime_type

        if content is not None:
            self._content = base64.b64encode(content).decode('UTF-8')

    @property
    def name(self):
        """
        Get the Name of attachment (displayed in email clients)
        :return the name
        :rtype str
        """
        return self._name

    @name.setter
    def name(self, val: str):
        """
        Set the Name of attachment (displayed in email clients)
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
        return self._mime_type

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
        Get ContentId for an Attachment. When set, used to embed an image within the body of an email message.
        :return the content id
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, val: str):
        """
        Set ContentId for an Attachment. When set, used to embed an image within the body of an email message.
        :param val: the content id
        :type val: str
        """
        self._content_id = val

    @property
    def content(self):
        """
        Get Content of an Attachment. The BASE64 encoded str containing the contents of an attachment.
        :return the BASE64 encoded string of content
        :rtype str
        """
        return self._content

    @content.setter
    def content(self, val: str):
        """
        Set Content of an Attachment. The BASE64 encoded str containing the contents of an attachment.
        :param val: the BASE64 encoded string of content
        :type val: str
        """
        self._content = val

    @property
    def custom_headers(self):
        """
        Get the list of custom message headers added to the attachment.
        :return list of CustomHeader
        :rtype list
        """
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, val: list):
        """
        Set the list of custom message headers added to the attachment.
        :param val: list of CustomHeader
        :type val: list
        """
        self._custom_headers = []
        if val is not None:
            for item in val:
                if isinstance(item, CustomHeader):
                    self._custom_headers.append(item)

    def add_custom_header(self, header, val: str = None):
        """
        Add a CustomHeader to the attachment
        :param header: the CustomHeader. CustomHeader, dict, and string is allowed
        :type header: CustomHeader, dict, str
        :param val: the custom header value, required if header is str
        :type val: str
        """
        if isinstance(header, CustomHeader):
            self._custom_headers.append(header)
        if isinstance(header, str):
            self._custom_headers.append(CustomHeader(header, val))
        if isinstance(header, dict):
            for name, value in header.items():
                self._custom_headers.append(CustomHeader(name, value))

    def readfile(self, file_path: str):
        """
        Read the specified file and get a str containing the resulting binary data.
        :param file_path: the file path to read
        :type: str
        """
        mimes = mimetypes.MimeTypes()
        with open(file_path, 'rb') as f:
            self._name = os.path.split(f.name)[1]
            mime = mimes.guess_type(f.name)
            if mime[0] is None:
                ext = os.path.splitext(f.name)[1][1:].strip()
                self._mime_type = self.__get_mime_type_from_ext(ext)
            else:
                self._mime_type = str(mime[0])
            data = f.read()
            self._content = base64.b64encode(data).decode('UTF-8')
            f.close()

    @staticmethod
    def __get_mime_type_from_ext(extension: str):
        """
        Takes a file extension, minus the '.', and returns the corresponding MimeType for the given extension.
        :param extension: the file extension
        :type extension: str
        :return the mime type
        :rtype str
        """
        switcher = {
            "txt": "text/plain",
            "ini": "text/plain",
            "sln": "text/plain",
            "cs": "text/plain",
            "js": "text/plain",
            "config": "text/plain",
            "vb": "text/plain",
            "jpg": "image/jpeg",
            "jpeg": "image/jpeg",
            "bmp": "image/bmp",
            "csv": "text/csv",
            "doc": "application/msword",
            "docx": "application/"
                    "vnd.openxmlformats-officedocument.wordprocessingml.document",
            "gif": "image/gif",
            "html": "text/html",
            "pdf": "application/pdf",
            "png": "image/png",
            "ppt": "application/vnd.ms-powerpoint",
            "pptx": "application/"
                    "vnd.openxmlformats-officedocument.presentationml.presentation",
            "xls": "application/vnd.ms-excel",
            "xlsx": "application/"
                    "vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "xml": "application/xml",
            "zip": "application/x-zip-compressed",
            "wav": "audio/wav",
            "eml": "message/rfc822",
            "mp3": "audio/mpeg",
            "mp4": "video/mp4",
            "mov": "video/quicktime"
        }
        return switcher.get(extension, "application/octet-stream")

    def __str__(self):
        """
        Get a str representation of this attachment.
        :return the string
        :rtype str
        """
        return str(self._name + ", " + self._mime_type)
