import json
from collections import OrderedDict

from ..sendresponse import SendResponse
from ..sendresult import SendResult
from .serialization.messageresultdto import MessageResultDto
from .serialization.injectionresponsedto import InjectionResponseDto


def determine_send_result(response_dto: InjectionResponseDto, response_code: int):
    """
    Enumerated SendResult of the payload response from the Injection Api
    :param response_dto: the response dto
    :type response_dto: InjectionResponseDto
    :param response_code: the Http Response code
    :type response_code: int
    :return the parsed result of the injection request
    :rtype SendResult
    """
    # HttpStatusCode.OK
    if response_code == 200:
        result_enum = SendResult[response_dto.error_code]
        if result_enum is None:
            return SendResult.UnknownError
        else:
            return result_enum

    # HttpStatusCode.InternalServerError
    elif response_code == 500:
        return SendResult.InternalError

    # HttpStatusCode.RequestTimeout
    elif response_code == 408:
        return SendResult.Timeout

    # HttpStatusCode.Unauthorized
    elif response_code == 401:
        return SendResult.InvalidAuthentication

    else:
        return SendResult.InvalidAuthentication


def get_injection_response_dto(response: str):
    """
    Get the InjectionResponseDto from the response str
    :param response: the Http response in string format
    :type response: str
    :return the converted injection response dto
    :rtype InjectionResponseDto
    """
    dct = json.loads(response, object_pairs_hook=OrderedDict)

    resp_dto = InjectionResponseDto()
    if 'ErrorCode' in dct:
        resp_dto._error_code = dct['ErrorCode']

    if 'TransactionReceipt' in dct:
        resp_dto._transaction_receipt = dct['TransactionReceipt']

    if 'MessageResults' in dct:
        resp_dto.message_results = []
        for item in dct['MessageResults'] or []:
            message_dto = MessageResultDto()
            if 'Index' in item:
                message_dto.index = item['Index']
            if 'AddressResults' in item:
                message_dto.address_results = str(item['AddressResults'])
            if 'ErrorCode' in item:
                message_dto.error_code = item['ErrorCode']
            resp_dto.message_results.append(message_dto)

    return resp_dto


class InjectionResponseParser(object):
    """
    Used by the HttpClient to convert the response form the Injection API.
    """

    @staticmethod
    def parse(response: str, response_code: int):
        """
        Parse the response from theInjection Api into SendResponse
        :param response: the Http response in string format
        :type response: str
        :param response_code: the Http Response code
        :type response_code: int
        :return the converted response
        :rtype SendResponse
        """
        injection_response = get_injection_response_dto(response)
        result_enum = determine_send_result(injection_response, response_code)
        new_response = SendResponse(result_enum)
        new_response.transaction_receipt = injection_response.transaction_receipt

        if result_enum == SendResult.Warning \
                and (injection_response.message_results and len(injection_response.message_results) > 0):
            new_response.result = SendResult[injection_response.message_results[0].error_code]

        if injection_response.message_results and len(injection_response.message_results) > 0:
            new_response.address_results = injection_response.message_results[0].address_results

        return new_response
