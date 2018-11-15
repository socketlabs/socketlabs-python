import random
import string
import sys

from socketlabs.injectionapi.message.bulkrecipient import BulkRecipient
from socketlabs.injectionapi.message.emailaddress import EmailAddress


class RandomHelper(object):

    def random_string(self, length: int = None, exclude_numbers: bool = False):
        if length is None:
            length = self.random_int()
        chars = string.ascii_uppercase + string.ascii_lowercase
        if not exclude_numbers:
            chars = chars + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def random_email_address(self, name_cnt: int = 8, domain_cnt: int = 8, suffix_cnt: int = 3):
        return EmailAddress(self.random_email_string(name_cnt, domain_cnt, suffix_cnt))

    def random_email_string(self, name_cnt: int = 8, domain_cnt: int = 8, suffix_cnt: int = 3):
        return "{name}@{domain}.{suffix}"\
            .format(
                name=self.random_string(name_cnt),
                domain=self.random_string(domain_cnt),
                suffix=self.random_string(suffix_cnt)
            )

    def random_int(self, min_range: int = 0, max_range: int = 500):
        if max_range > sys.maxsize:
            max_range = sys.maxsize - 1
        if min_range > max_range:
            raise Exception("The min value must be less than the max value.")
        return random.randint(min_range, max_range + 1)

    def random_server_id(self):
        return self.random_int(1001, 21000)

    def random_list_of_email_addresses(self, count: int):
        emails = []
        for _ in range(count):
            emails.append(EmailAddress(self.random_email_string()))
        return emails

    def random_list_of_bulk_recipients(self, count: int):
        recipients = []
        for _ in range(count):
            recipients.append(BulkRecipient(self.random_email_string()))
        return recipients
