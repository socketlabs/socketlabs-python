from http import HTTPStatus
from http.client import HTTPException
from ..retrysettings import RetrySettings
from .httprequest import HttpRequest
from .serialization.injectionrequest import InjectionRequest
import socket
import time


class RetryHandler(object):
    attempts = 0
    ErrorStatusCodes = [
        HTTPStatus.INTERNAL_SERVER_ERROR,
        HTTPStatus.BAD_GATEWAY,
        HTTPStatus.SERVICE_UNAVAILABLE,
        HTTPStatus.GATEWAY_TIMEOUT
    ]
    Exceptions = [
        socket.timeout,
        HTTPException
    ]

    def __init__(self, http_client: HttpRequest, settings: RetrySettings):

        self.__http_client = http_client
        self.__retry_settings = settings

    def send(self, body):

        if self.__retry_settings.maximum_number_of_retries == 0:
            return self.__http_client.send_request(body)

        while True:
            wait_interval = self.__retry_settings.get_next_wait_interval(self.attempts)

            try:

                response = self.__http_client.send_request(body)

                if response.status in self.ErrorStatusCodes:
                    raise HTTPException("HttpStatusCode: {0}. Response contains server error.".format(response.status))

                return response

            except socket.timeout:

                self.attempts += 1

                if self.attempts > self.__retry_settings.maximum_number_of_retries:
                    raise socket.timeout
                time.sleep(wait_interval.seconds)

            except HTTPException:

                self.attempts += 1

                if self.attempts > self.__retry_settings.maximum_number_of_retries:
                    raise HTTPException
                time.sleep(wait_interval.seconds)

    def send_async(self, request: InjectionRequest, on_success_callback, on_error_callback):

        wait_interval = self.__retry_settings.get_next_wait_interval(self.attempts)

        def on_success(response):

            if response.status in self.ErrorStatusCodes and self.attempts < self.__retry_settings.maximum_number_of_retries:

                self.attempts += 1
                time.sleep(wait_interval.seconds)
                self.send_async(request, on_success_callback, on_error_callback)

            else:
                on_success_callback(response)

        def on_error(exception):

            if exception in self.Exceptions and self.attempts < self.__retry_settings.maximum_number_of_retries:

                self.attempts += 1
                time.sleep(wait_interval.seconds)
                self.send_async(request, on_success_callback, on_error_callback)

            else:

                self.attempts = self.__retry_settings.maximum_number_of_retries + 1
                on_error_callback(exception)

        self.__http_client.send_async_request(request, on_success, on_error)
