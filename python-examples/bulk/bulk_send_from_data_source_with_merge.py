import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    BulkMessage, BulkRecipient, EmailAddress

"""
For our example we are using a mock repository class (Customer and 
CustomerRepository) that returns hard-coded data. Normally the 
repository class would access a database to retrieve this data.
"""


class Customer(object):

    def __init__(self, first: str, last: str, email: str, color: str):
        self._first_name = first
        self._last_name = last
        self._email_address = email
        self._favorite_color = color

    @property
    def first_name(self):
        return str(self._first_name)

    @first_name.setter
    def first_name(self, val: str):
        self._first_name = val

    @property
    def last_name(self):
        return str(self._last_name)

    @last_name.setter
    def last_name(self, val: str):
        self._last_name = val

    @property
    def email_address(self):
        return str(self._email_address)

    @email_address.setter
    def email_address(self, val: str):
        self._email_address = val

    @property
    def favorite_color(self):
        return str(self._favorite_color)

    @favorite_color.setter
    def favorite_color(self, val: str):
        self._favorite_color = val


class CustomerRepository(object):

    @staticmethod
    def get_customer_repo():
        return [
            Customer("Recipient", "One", "recipient1@example.com", "Green"),
            Customer("Recipient", "Two", "recipient2@example.com", "Red"),
            Customer("Recipient", "Three", "recipient3@example.com", "Blue"),
            Customer("Recipient", "Four", "recipient4@example.com", "Orange")
        ]


# build the message
message = BulkMessage()

message.subject = "Sending A Test Message With Merge Data From Datasource"
message.html_body = "<html>" \
                     "   <body>" \
                     "       <h1>Sending A Test Message With Merge Data From Datasource</h1>" \
                     "       <h2>Hello %%FirstName%% %%LastName%%.</h2>" \
                     "       <p>Is your favorite color still %%FavoriteColor%%?</p>" \
                     "   </body>" \
                     "</html>"
message.plain_text_body = "Sending A Test Message With Merge Data From Datasource" \
                     "       Hello %%FirstName%% %%LastName%%. Is your favorite color still %%FavoriteColor%%?"

message.from_email_address = EmailAddress("from@example.com")

customers = CustomerRepository.get_customer_repo()

for customer in customers:
    recipient = BulkRecipient(customer.email_address, "{first} {last}".format(
                                  first=customer.first_name,
                                  last=str(customer.last_name)))
    recipient.add_merge_data("FirstName", customer.first_name)
    recipient.add_merge_data("LastName", customer.last_name)
    recipient.add_merge_data("FavoriteColor", customer.favorite_color)

    message.add_to_recipient(recipient)


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))
