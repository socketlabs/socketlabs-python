import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    BulkMessage, BulkRecipient, EmailAddress


# build the message
message = BulkMessage()

message.subject = "Sending A Test Message With Merge Data"
message.html_body = "<html>" \
                     "   <head><title>Sending A Test Message With Merge Data</title></head>" \
                     "   <body>" \
                     "       <h1>Sending A Complex Test Message</h1>" \
                     "       <h2>Global Merge Data</h2>" \
                     "       <p>Motto = <b>%%Motto%%</b></p>" \
                     "       <h2>Per Recipient Merge Data</h2>" \
                     "       <p>" \
                     "       EyeColor = %%EyeColor%%<br/>" \
                     "       HairColor = %%HairColor%%" \
                     "       </p>" \
                     "   </body>" \
                     "</html>"
message.plain_text_body = "Sending A Test Message With Merge Data" \
                     "       Merged Data" \
                     "           Motto = %%Motto%%" \
                     "       " \
                     "       Example of Merge Usage" \
                     "           EyeColor = %%EyeColor%%" \
                     "           HairColor = %%HairColor%%"

message.from_email_address = EmailAddress("from@example.com")


# Add some global merge-data (These will be applied to all Recipients
# unless specifically overridden by Recipient level merge-data)
message.add_global_merge_data("EyeColor", "{ not set }")
message.add_global_merge_data("HairColor", "{ not set }")
message.add_global_merge_data("Motto", "When hitting the Inbox matters!")

# Add recipients with merge data
recipient1 = BulkRecipient("recipient1@example.com")
recipient1.add_merge_data("EyeColor", "Blue")
recipient1.add_merge_data("HairColor", "Blond")
message.add_to_recipient(recipient1)

recipient2 = BulkRecipient("recipient2@example.com", "Recipient #2")
recipient2.add_merge_data("EyeColor", "Green")
message.add_to_recipient(recipient2)

recipient3 = BulkRecipient("recipient3@example.com")
recipient3.add_merge_data("HairColor", "Brown")
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
