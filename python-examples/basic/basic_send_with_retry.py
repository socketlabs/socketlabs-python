import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.proxy import Proxy
from socketlabs.injectionapi.message.__imports__ import BasicMessage, EmailAddress

def on_success(response):
    """
    Handle the success response from the client
    :param response: the SendResponse
    :return: SendResponse
    """
    print(json.dumps(response.to_json(), indent=2))


def on_error(exception):
    """
    Handle the error response from the client
    :param exception: the Exception
    :return: Exception
    """
    print(exception) 

# build the message
message = BasicMessage()

message.subject = "Sending An Email Through A Proxy"
message.html_body = "<html><body>" \
                    "<h1>Sending An Email Through A Proxy</h1>" \
                    "<p>This is the Html Body of my message.</p>" \
                    "</body></html>"
message.plain_text_body = "This is the Plain Text Body of my message."

message.from_email_address = EmailAddress("from@example.com")
message.add_to_email_address("recipient@example.com")


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the proxy
proxy = Proxy("127.0.0.1", 4433)

# create the client
client = SocketLabsClient(server_id, api_key, proxy)
client.request_timeout = 10
client.number_of_retries = 2

# send the message
response = client.send(message)
client.send_async(message, on_success, on_error)

print(json.dumps(response.to_json(), indent=2))
