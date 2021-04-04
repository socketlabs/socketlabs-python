from http import HTTPStatus
from ..retrysettings import RetrySettings
from .httprequest import HttpRequest
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

        return