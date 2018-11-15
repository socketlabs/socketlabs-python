class StringExtension(object):

    @staticmethod
    def is_none_or_white_space(val: str):
        """
        Check if the string is None or Whitespace
        :param val: string to validate
        :type val: str
        :return the result
        :rtype bool
        """
        if val is None:
            return True
        if val.strip() == '':
            return True
        return False

    @staticmethod
    def find_character_in_string(val: str, ch: str):
        """
        find a character in a string
        :param val: value to check
        :type val: str
        :param ch: character to look for
        :type ch: str
        :return the result
        :rtype bool
        """
        for i, ltr in enumerate(val):
            if ltr == ch:
                yield i

    @staticmethod
    def is_valid_email_address(email_address: str):
        """
        Determines if the EmailAddress is valid. Does simple syntax validation on the email address.
        :return bool
        """
        if email_address is None:
            return False

        # 320 used over 256 to be more lenient
        if len(email_address) > 320:
            return False

        parts = email_address.split('@')
        if len(parts) != 2:
            return False

        if len(parts[0].strip()) < 1:
            return False
        if len(parts[1].strip()) < 1:
            return False

        badChars = list(StringExtension.find_character_in_string(email_address, ","))
        badChars.extend(list(StringExtension.find_character_in_string(email_address, ' ')))
        badChars.extend(list(StringExtension.find_character_in_string(email_address, ';')))
        return len(badChars) == 0