from .stringextension import StringExtension
from .apikeyparseresult import ApiKeyParseResult

class ApiKeyParser(object):
    """
    Wrapper of the Http Client to handle threading for async
    """

    def parse(self, whole_api_key: str):
        """
        Parse the API key to determine what kind of key was provided.
        :param whole_api_key: A ApiKeyParseResult with the parsing results
        :type whole_api_key: string
        :return the ApiKeyParseResult from the request
        :rtype ApiKeyParseResult
        """

        if StringExtension.is_none_or_white_space(whole_api_key):
            return ApiKeyParseResult.InvalidEmptyOrWhitespace

        if len(whole_api_key) != 61:
            return ApiKeyParseResult.InvalidKeyLength

        if whole_api_key.index('.') == -1:
            return ApiKeyParseResult.InvalidKeyFormat

        public_part_end = whole_api_key[0:50].index('.')
        if public_part_end == -1:
            return ApiKeyParseResult.InvalidUnableToExtractPublicPart

        public_part = whole_api_key[0:public_part_end]
        if len(public_part) != 20:
            return ApiKeyParseResult.InvalidPublicPartLength

        if len(whole_api_key) <= public_part_end + 1:
            return ApiKeyParseResult.InvalidUnableToExtractSecretPart

        private_part = whole_api_key[public_part_end + 1:len(whole_api_key)]
        if len(private_part) != 40:
            return ApiKeyParseResult.InvalidSecretPartLength

        return ApiKeyParseResult.Success
