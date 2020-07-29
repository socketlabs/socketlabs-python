import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    BasicMessage, EmailAddress

#   For more information on AMP Html, visit the following link: amp.dev/documentation

# build the message
message = BasicMessage()

message.subject = "Sending A Test Message (Basic Send)"

message.html_body = "<html><body>" \
                    "<h1>This HTML will show if AMP is not supported on the receiving end of the email.</h1>" \
                    "<p>This is the Html Body of my message.</p>" \
                    "</body></html>"
message.amp_body = "<!doctype html>" \
                   "<html amp4email>" \
                   "<head>" \
                   "  <meta charset=\"utf-8\">" \
                   "  <script async src=\"https://cdn.ampproject.org/v0.js\"></script>" \
                   "  <style amp4email-boilerplate>body{visibility:hidden}</style>" \
                   "  <style amp-custom>" \
                   "    h1 {" \
                   "      margin: 1rem;" \
                   "    }" \
                   "  </style>" \
                   "</head>" \
                   "<body>" \
                   "  <h1>This is the AMP Html Body of my message</h1>" \
                   "</body>" \
                   "</html>"

message.from_email_address = EmailAddress("from@example.com")
message.add_to_email_address("recipient1@example.com")
message.add_to_email_address("recipient2@example.com", "Recipient #2")
message.add_to_email_address(EmailAddress("recipient3@example.com"))
message.add_to_email_address(EmailAddress("recipient4@example.com", "Recipient #4"))


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))
