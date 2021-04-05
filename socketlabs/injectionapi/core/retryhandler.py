from http import HTTPStatus
from ..retrysettings import RetrySettings
from .httprequest import HttpRequest
from .injectionresponseparser import InjectionResponseParser
import sys
import socket
import time

class RetryHandler(object):

    ErrorStatusCodes = [
        HTTPStatus.INTERNAL_SERVER_ERROR,
        HTTPStatus.BAD_GATEWAY,
        HTTPStatus.SERVICE_UNAVAILABLE,
        HTTPStatus.GATEWAY_TIMEOUT
    ]

    def __init__(self, http_client: HttpRequest, settings: RetrySettings):

        self.__http_client = http_client
        self.__retry_settings = settings
    
    def send(self, body):

        if self.__retry_settings.maximum_number_of_retries == 0:
            return self.__http_client.send_request(body)

        attempts = 0
        while True:
            wait_interval = self.__retry_settings.get_next_wait_interval(attempts)

            try:
                response = self.__http_client.send_request(body)

                if response.status in self.ErrorStatusCodes:
                    raise Exception("Server Error")
                
                data = response.read().decode("utf-8")
                response_code = response.status
                result = InjectionResponseParser.parse(data, response_code)

                return result
            
            except socket.timeout:
                attempts += 1
                print("Retry Attempt : ", sys.exc_info()[0])
                if attempts > self.__retry_settings.maximum_number_of_retries:
                    raise socket.timeout
                time.sleep(wait_interval.seconds)
            
