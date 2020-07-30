import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    Attachment, BulkMessage, BulkRecipient, CustomHeader, EmailAddress


# build the message
message = BulkMessage()

message.message_id = "ComplexExample"
message.mailing_id = "BulkSend"

message.charset = "UTF-8"

message.subject = "Sending A Complex Bulk Test Message"
message.html_body = "<html>" \
                    "   <head><title>Sending A Complex Bulk Test Message</title></head>" \
                    "   <body>" \
                    "       <h1>Sending A Complex Test Message</h1>" \
                    "       <h2>Merge Data</h2>" \
                    "       <p>" \
                    "           Motto = <b>%%Motto%%</b> </br>" \
                    "           Birthday = <b>%%Birthday%%</b> </br>" \
                    "           Age = <b>%%Age%%</b> </br>" \
                    "           UpSell = <b>%%UpSell%%</b>" \
                    "       </p>" \
                    "       <h2>Example of Merge Usage</h2>" \
                    "       <p>" \
                    "           Our company motto is '<b>%%Motto%%</b>'. </br>" \
                    "           Your birthday is <b>%%Birthday%%</b> and you are <b>%%Age%%</b> years old." \
                    "       </p>" \
                    "       <h2>UTF-8 Characters:</h2>" \
                    "       <p>✔ - Check</p>" \
                    "       <h2>Embedded Image:</h2>" \
                    "       <p><img src='cid:bus' /></p>" \
                    "   </body>" \
                    "</html>"
message.plain_text_body = "Sending A Complex Bulk Test Message" \
                    "       Merged Data" \
                    "           Motto = %%Motto%%" \
                    "           Birthday = %%Birthday%%" \
                    "           Age = %%Age%%" \
                    "           UpSell = %%UpSell%%" \
                    "       " \
                    "       Example of Merge Usage" \
                    "           Our company motto is '%%Motto%%'." \
                    "           Your birthday is %%Birthday%% and you are %%Age%% years old."
message.amp_body = "<!doctype html>"\
                 "<html amp4email>" \
                 "<head>"\
                 "<title>Sending an AMP Test Message</title>"\
                 "  <meta charset=\"utf-8\">"\
                 "  <script async src=\"https://cdn.ampproject.org/v0.js\"></script>"\
                 "  <style amp4email-boilerplate>body{visibility:hidden}</style>"\
                 "  <style amp-custom>"\
                 "    h1 {"\
                 "      margin: 1rem;"\
                 "    }"\
                 "  </style>"\
                 "</head>"\
                 "<body>"\
                 "       <h1>Sending An AMP Complex Test Message</h1>"\
                 "       <h2>Merge Data</h2>"\
                 "       <p>"\
                 "           Motto = <b>%%Motto%%</b> </br>"\
                 "           Birthday = <b>%%Birthday%%</b> </br>"\
                 "           Age = <b>%%Age%%</b> </br>"\
                 "           UpSell = <b>%%UpSell%%</b>"\
                 "       </p>"\
                 "       <h2>Example of Merge Usage</h2>"\
                 "       <p>"\
                 "           Our company motto is '<b>%%Motto%%</b>'. </br>"\
                 "           Your birthday is <b>%%Birthday%%</b> and you are <b>%%Age%%</b> years old."\
                 "       </p>"\
                 "       <h2>UTF-8 Characters:</h2>"\
                 "       <p>✔ - Check</p>"\
                 "       </body>"\
                 "       </html>"

message.from_email_address = EmailAddress("from@example.com", "FromMe")
message.reply_to_email_address = EmailAddress("replyto@example.com")


# Add some global merge-data
# (These will be applied to all Recipients unless specifically overridden by Recipient level merge data)
# ==========================
# Add global merge data using a dictionary
global_merge_data = {
        "Motto": "When hitting the inbox matters!",
        "Birthday": "unknown"
    }
message.global_merge_data = global_merge_data

# Add global merge data directly to the dictionary on the message
message.global_merge_data["Age"] = "an unknown number of"

# Add global merge data  using the add_global_merge_data function
message.add_global_merge_data("UpSell", "BTW:  You are eligible for discount pricing when you upgrade your service!")


# Add recipients with merge data
# Including merge data on the recipient with the same name as the global merge data will override global merge data
# ==========================
# Add recipients with merge data using a dictionary
rec1_merge_data = {
        "Birthday": "08/05/1991",
        "Age": "27"
    }
message.to_recipient.append(BulkRecipient("recipient1@example.com", merge_data=rec1_merge_data))

# Add recipients merge data directly to the dictionary
recipient2 = BulkRecipient("recipient2@example.com", "Recipient #2")
recipient2.merge_data["Birthday"] = "04/12/1984"
recipient2.merge_data["Age"] = "34"
recipient2.merge_data["UpSell"] = ""
message.add_to_recipient(recipient2)

# Add recipients merge data using the add_merge_data function
recipient3 = BulkRecipient("recipient3@example.com")
recipient3.add_merge_data("Birthday", "10/30/1978")
recipient3.add_merge_data("Age", "40")
recipient3.add_merge_data("UpSell", "")
recipient3.friendly_name = "Recipient 3"
message.add_to_recipient(recipient3)

message.add_to_recipient(BulkRecipient("recipient4@example.com", "Recipient #4"))


# Adding Attachments
# ==========================
# Add Attachment directly to the list
attachments = [
    Attachment(name="bus.png", mime_type="image/png", file_path="../img/bus.png")
]
message.attachments = attachments

# Add Attachment using the add_attachment function
attachment2 = Attachment(name="bus2", mime_type="image/png", file_path="../img/bus.png")
attachment2.content_id = "bus"
message.add_attachment(attachment2)

# Add Attachment using a filePath
message.add_attachment(Attachment(file_path="../html/SimpleEmail.html"))

# Add Attachment using bytes of the file
with open("../img/bus.png", 'rb') as f:
    data = f.read()
    f.close()
attachment4 = Attachment(name="yellow-bus.png", mime_type="image/png", content=data)

# Add CustomHeaders to Attachment
attachment4.custom_headers.append(CustomHeader("Color", "Yellow"))
attachment4.add_custom_header("Place", "Beach")

message.add_attachment(attachment4)


# Adding Custom Headers
# ==========================
# Add CustomHeader using a list
headers = [
    CustomHeader("example-type", "bulk-send-complex-example"),
    CustomHeader("message-contains", "attachments, headers")
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
