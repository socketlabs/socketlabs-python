import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    BasicMessage, CustomHeader, EmailAddress


# build the message
message = BasicMessage()

message.subject = "Sending An Email With Custom Headers"
message.html_body = "<html><body>" \
                    "<h1>Sending An Email With Custom Headers</h1>" \
                    "<p>This is the Html Body of my message.</p>" \
                    "</body></html>"
message.plain_text_body = "This is the Plain Text Body of my message."

message.from_email_address = EmailAddress("from@example.com")
message.add_to_email_address("recipient@example.com")


# Add CustomHeader using a list
headers = [
    CustomHeader("example-type", "basic-send-with-custom-headers"),
    CustomHeader("message-contains", "headers")
]
message.custom_headers = headers

# Add CustomHeader directly to the list
message.custom_headers.append(CustomHeader("message-has-attachments", "true"))

# Add CustomHeader using the add_custom_header function
message.add_custom_header("testMessageHeader", "I am a message header")


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))
