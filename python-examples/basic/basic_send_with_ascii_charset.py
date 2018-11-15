import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    BasicMessage, EmailAddress


# build the message
message = BasicMessage()

message.subject = "Sending A ASCII Charset Email"
message.html_body = "<html><body>" \
                    "<h1>Sending A ASCII Charset Email</h1>" \
                    "<p>This is the html Body of my message.</p>" \
                    "<h2>UTF-8 Characters:</h2><p>✔ - Check</p>" \
                    "</body></html>"
message.plain_text_body = "This is the Plain Text Body of my message."

# Set the CharSet
message.charset = "ASCII"

message.from_email_address = EmailAddress("from@example.com")
message.add_to_email_address("recipient@example.com")


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))
