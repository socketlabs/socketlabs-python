"""
SocketLabsClient is a wrapper for the SocketLabs Injection API that makes 
it easy to send messages and parse responses.
"""
from .core.httpendpoint import HttpEndpoint
from .core.httprequest import HttpRequest
from .core.injectionrequestfactory import InjectionRequestFactory
from .core.sendvalidator import SendValidator
from .message.basicmessage import BasicMessage
from .message.bulkmessage import BulkMessage
from .proxy import Proxy
from .sendresult import SendResult


class SocketLabsClient(object):
    """
    SocketLabsClient is a wrapper for the SocketLabs Injection API that makes
    it easy to send messages and parse responses.
    """

    def __init__(self, server_id: int, api_key: str, proxy: Proxy = None):
        """
        Creates a new instance of the SocketLabsClient.
        :param server_id: Your SocketLabs ServerId number.
        :type server_id: str
        :param api_key: Your SocketLabs Injection API key.
        :type api_key: str
        :param proxy: The Proxy you would like to use.
        :type proxy: str
        """
        self._server_id = server_id
        self._api_key = api_key
        self._http_proxy = proxy

    @property
    def __endpoint(self):
        """
        The SocketLabs Injection API endpoint
        :return the Http Endpoint for the request
        :rtype HttpEndpoint
        """
        return HttpEndpoint("inject.socketlabs.com", "/api/v1/email")

    @property
    def __proxy(self):
        """
        The Proxy you would like to use.
        :return the optional proxy to use for the request
        :rtype Proxy
        """
        return self._http_proxy

    def __build_http_request(self):
        """
        Build the HttpRequest. Will add the proxy, if set
        :return the HttpRequest object to use for the request
        :rtype HttpRequest
        """
        req = HttpRequest(HttpRequest.HttpRequestMethod.POST, self.__endpoint)
        if self._http_proxy is not None:
            req.proxy = self._http_proxy
        return req

    def send(self, message):
        """
        Sends a BasicMessage message and returns the response from the Injection API.
        :param message: A BasicMessage object to be sent.
        :type message: object
        :return the SendResponse from the request
        :rtype SendResponse
        """
        if isinstance(message, BasicMessage):
            return self.__send_basic_message(message)
        elif isinstance(message, BulkMessage):
            return self.__send_bulk_message(message)
        else:
            raise Exception('Message type was not BasicMessage, BulkMessage. Send Failed')

    def __send_basic_message(self, message: BasicMessage):
        """
        Sends a BasicMessage message and returns the response from the Injection API.
        :param message: A BasicMessage object to be sent.
        :type message: BasicMessage
        :return the SendResponse from the request
        :rtype SendResponse
        """
        resp = self.__validate_basic_message(message)
        if not resp.result == SendResult.Success:
            return resp

        req_factory = InjectionRequestFactory(self._server_id, self._api_key)
        body = req_factory.generate_request(message)

        request = self.__build_http_request()
        result = request.send_request(body)
        return result

    def __send_bulk_message(self, message: BulkMessage):
        """
        Sends a BulkMessage message and returns the response from the Injection API.
        :param message: A BulkMessage object to be sent.
        :type message: BulkMessage
        :return the SendResponse from the request
        :rtype SendResponse
        """
        resp = self.__validate_bulk_message(message)
        if not resp.result == SendResult.Success:
            return resp

        req_factory = InjectionRequestFactory(self._server_id, self._api_key)
        body = req_factory.generate_request(message)

        request = self.__build_http_request()
        result = request.send_request(body)
        return result

    def send_async(self, message: BasicMessage, on_success, on_error):
        """
        Send an BasicMessage message asynchronously
        :param message: a BasicMessage object to be sent
        :type message: BasicMessage
        :param on_success: success callback method
        :type on_success: object
        :param on_error: error callback method
        :type on_error: object
        """
        if isinstance(message, BasicMessage):
            self.__send_basic_message_async(message, on_success, on_error)
        elif isinstance(message, BulkMessage):
            self.__send_bulk_message_async(message, on_success, on_error)
        else:
            raise Exception('Message type was not BasicMessage, BulkMessage. Send Failed')

    def __send_basic_message_async(self, message: BasicMessage, on_success, on_error):
        """
        Send an BasicMessage message asynchronously
        :param message: a BasicMessage object to be sent
        :type message: BasicMessage
        :param on_success: success callback method
        :type on_success: object
        :param on_error: error callback method
        :type on_error: object
        """
        resp = self.__validate_basic_message(message)
        if not resp.result == SendResult.Success:
            return resp

        req_factory = InjectionRequestFactory(self._server_id, self._api_key)
        body = req_factory.generate_request(message)

        request = self.__build_http_request()
        request.send_async_request(body, on_success, on_error)

    def __send_bulk_message_async(self, message: BulkMessage, on_success, on_error):
        """
        Send an BulkMessage message asynchronously
        :param message: a BulkMessage object to be sent
        :type message: BulkMessage
        :param on_success: success callback method
        :type on_success: object
        :param on_error: error callback method
        :type on_error: object
        """
        resp = self.__validate_bulk_message(message)
        if not resp.result == SendResult.Success:
            return resp

        req_factory = InjectionRequestFactory(self._server_id, self._api_key)
        body = req_factory.generate_request(message)

        request = self.__build_http_request()
        request.send_async_request(body, on_success, on_error)

    def __validate_basic_message(self, message: BasicMessage):
        """
        Validate a BulkMessage message
        :param message: a BasicMessage object to be sent
        :type message: BasicMessage
        """
        resp = SendValidator.validate_credentials(self._server_id, self._api_key)
        if not resp.result == SendResult.Success:
            return resp

        return SendValidator.validate_message(message)

    def __validate_bulk_message(self, message: BulkMessage):
        """
        Validate a BulkMessage message
        :param message: a BulkMessage object to be sent
        :type message: BulkMessage
        """
        resp = SendValidator.validate_credentials(self._server_id, self._api_key)
        if not resp.result == SendResult.Success:
            return resp

        return SendValidator.validate_message(message)
