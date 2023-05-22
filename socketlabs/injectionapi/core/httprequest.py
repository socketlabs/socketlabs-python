import http
import http.client
import json
import threading
import sys
import queue
from enum import Enum

from ..version import __version__
from ..proxy import Proxy

from .stringextension import StringExtension
from .httpendpoint import HttpEndpoint
from .injectionresponseparser import InjectionResponseParser
from .serialization.injectionrequest import InjectionRequest


class HttpRequest(object):
    """
    Wrapper of the Http Client to handle threading for async
    """

    class HttpRequestMethod(Enum):
        """
        Enumeration of HTTP Request Methods
        """
        GET = 0
        POST = 1
        PUT = 2
        DELETE = 3

    def __init__(self, method: HttpRequestMethod, endpoint: HttpEndpoint, timeout: int, authentication: str):
        """
        Creates a new instance of the HTTP Request class
        :param method: the HTTP request method
        :type method: HttpRequestMethod
        :param endpoint: the Http endpoint for the HTTP request
        :type endpoint: HttpEndpoint
        """
        self._request_method = method
        self._endpoint = endpoint
        self._http_proxy = None
        self._timeout = timeout
        self._authentication = authentication
        self._headers = {
            'User-Agent': self.__user_agent,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json',
        }
        if not StringExtension.is_none_or_white_space(authentication):
            self._headers["Authorization"] = "Bearer " + authentication

    @property
    def __user_agent(self):
        """
        The User-Agent request header added to the Injection API Http request.
        Used to identify the source of the request.
        :return the SocketLabs User-Agent
        :rtype str
        """
        return "SocketLabs-python/{0};python({1})".format(__version__, sys.version.split(' ')[0])

    @property
    def __request_method(self):
        """
        The HTTP Request Method to use
        :return the HTTP request method
        :rtype HttpRequestMethod
        """
        return self._request_method

    @property
    def __endpoint(self):
        """
        The SocketLabs Injection API endpoint
        :return the Http endpoint for the HTTP request
        :rtype HttpEndpoint
        """
        return self._endpoint

    @property
    def __timeout(self):
        """
        The SocketLabs Injection API timeout
        :return the Http timeout for the HTTP request
        :rtype int
        """ 
        return self._timeout       

    @property
    def proxy(self):
        """
        Get the Proxy to use when making the HTTP request
        :return the Proxy to use for the HTTP request
        :rtype Proxy
        """
        return self._http_proxy

    @proxy.setter
    def proxy(self, val: Proxy):
        """
        Set the Proxy to use when making the HTTP request
        :param val: the Proxy to use for the HTTP request
        :type val: Proxy
        """
        self._http_proxy = val

    def send_async_request(self, request: InjectionRequest, on_success_callback, on_error_callback):
        """
        Send an HTTP Request asynchronously
        :param request: the injection request to send
        :type request: InjectionRequest
        :param on_success_callback: the callback method for success
        :type on_success_callback: method
        :param on_error_callback: the callback method for error
        :type on_error_callback: method
        """

        try:
            print (request)
            th = threading.Thread(target=self.__queue_request,
                                  kwargs={
                                      "request": request,
                                      "on_success_callback": on_success_callback,
                                      "on_error_callback": on_error_callback
                                  })
            th.start()
            
        except Exception as e:
            on_error_callback(e)

    def __queue_request(self, request: InjectionRequest, on_success_callback, on_error_callback):
        """
        queue method for the threaded send request.
        :param request: the injection request to send
        :type request: InjectionRequest
        :param out_queue: the Queue object to handle the response
        :type out_queue: Queue
        """
        try:
            response = self.send_request(request)
            on_success_callback(response)

        except Exception:
            on_error_callback(sys.exc_info()[0])

    def send_request(self, request: InjectionRequest):
        """
        Send the HTTP Request
        :param request: the injection request to send
        :type request: InjectionRequest
        :return the injection response received from the request
        :rtype InjectionResponse
        """

        json_body = json.dumps(request.to_json())

        try:
            connection = self.__get_connection()
            connection.request("POST", self._endpoint.url, json_body, self._headers)
            response = connection.getresponse()

        except Exception as e:
            raise e

        return response

    def __get_connection(self):
        """
        Opens a socket connection to the server to set up an HTTP request.
        :return the HTTPS connection to use in the request
        :rtype HTTPSConnection
        """
        if self._http_proxy is not None:
            connection = http.client.HTTPSConnection(self._http_proxy.host, self._http_proxy.port, timeout=self.__timeout)
            connection.set_tunnel(self._endpoint.host, 443)
        else:
            connection = http.client.HTTPSConnection(self._endpoint.host, timeout=self.__timeout)

        return connection
