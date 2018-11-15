# -*- coding: utf-8 -*-
import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    BulkMessage, BulkRecipient, EmailAddress


# build the message
message = BulkMessage()

message.subject = "Sending A Test Message With ASCII Charset Merge Data"

# Set HTML and plain text body, both of which use UTF-8 characters
# Build the Content (Note the %% symbols used to denote the data to be merged)
message.html_body = "<html>" \
                     "   <body>" \
                     "       <h1>Sending A Test Message With ASCII Charset Merge Data</h1>" \
                     "       <h2>Merge Data</h2>" \
                     "       <p>Complete? = %%Complete%%</p>" \
                     "   </body>" \
                     "</html>"
message.plain_text_body = "Sending A Test Message With ASCII Charset Merge Data" \
                     "       Merged Data" \
                     "           Complete? = %%Complete%%"

message.from_email_address = EmailAddress("from@example.com")

# set the charset
message.charset = "ASCII"

message.add_global_merge_data("Complete", "{ no response }")

# Add recipients with merge data that contains UTF-8 characters
recipient1 = BulkRecipient("recipient1@example.com")
recipient1.add_merge_data("Complete", "✘")
message.add_to_recipient(recipient1)

recipient2 = BulkRecipient("recipient2@example.com", "Recipient #2")
recipient2.add_merge_data("Complete", "✔")
message.add_to_recipient(recipient2)

recipient3 = BulkRecipient("recipient3@example.com")
recipient3.add_merge_data("Complete", "✘")
message.add_to_recipient(recipient3)

message.add_to_recipient(BulkRecipient("recipient4@example.com", "Recipient #4"))


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))
