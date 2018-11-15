import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    BulkMessage, BulkRecipient, EmailAddress


# build the message
message = BulkMessage()

message.subject = "Sending A Test Message (Bulk Send)"
message.html_body = "<html><body>" \
                    "<h1>Sending A Test Message</h1>" \
                    "<p>This is the Html Body of my message.</p>" \
                    "</body></html>"
message.plain_text_body = "This is the Plain Text Body of my message."

message.from_email_address = EmailAddress("from@example.com")
message.add_to_recipient("recipient1@example.com")
message.add_to_recipient("recipient2@example.com", "Recipient #2")
message.add_to_recipient(BulkRecipient("recipient3@example.com"))
message.add_to_recipient(BulkRecipient("recipient4@example.com", "Recipient #4"))


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))
