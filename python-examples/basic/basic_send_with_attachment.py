import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    Attachment, BasicMessage, EmailAddress


# build the message
message = BasicMessage()

message.subject = "Sending An Email With An Attachment"
message.html_body = "<html><body>" \
                    "<h1>Sending An Email With An Attachment</h1>" \
                    "<p>This is the Html Body of my message.</p>" \
                    "</body></html>"
message.plain_text_body = "This is the Plain Text Body of my message."

message.from_email_address = EmailAddress("from@example.com")
message.add_to_email_address("recipient@example.com")


# Adding Attachments
# ==========================
# Add Attachment directly to the list
attachment = Attachment(name="bus.png", mime_type="image/png", file_path="../img/bus.png")

message.add_attachment(attachment)


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))
