import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    BasicMessage, EmailAddress

# build the message
message = BasicMessage()

message.subject = "Sending A Test Message"
message.html_body = "<html><body>" \
                    "<h1>Sending A Test Message</h1>" \
                    "<p>This is the Html Body of my message.</p>" \
                    "</body></html>"
message.plain_text_body = "This is the Plain Text Body of my message."

message.from_email_address = EmailAddress("from@example.com")

# good
message.to_email_address.append(EmailAddress("recipient@example.com"))

# invalid
message.to_email_address.append(EmailAddress("!@#$!@#$!@#$@#!$"))
message.to_email_address.append(EmailAddress("failure.com"))
message.to_email_address.append(EmailAddress("ImMissingSomething"))
message.to_email_address.append(EmailAddress("Fail@@!.Me"))


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))
