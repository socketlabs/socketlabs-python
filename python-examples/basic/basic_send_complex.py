import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    Attachment, BasicMessage, CustomHeader, EmailAddress, Metadata


# build the message
message = BasicMessage()

message.message_id = "ComplexExample"
message.mailing_id = "BasicSend"

message.subject = "Sending A Complex Test Message"
message.html_body = "<html><body>" \
                    "<h1>Sending A Complex Test Message</h1>" \
                    "<p>This is the html Body of my message.</p>" \
                    "<h2>Embedded Image:</h2>" \
                    "<p><img src='cid:bus' /></p>" \
                    "</body></html>"
message.plain_text_body = "This is the Plain Text Body of my message."

# Setting AMP Body
message.setAmpBody = "<!doctype html>" \
                   "<html amp4email>" \
                   "    <head>" \
                   "    <meta charset=\"utf-8\">" \
                   "     <script async src=\"https://cdn.ampproject.org/v0.js\"></script>" \
                   "    <style amp4email-boilerplate>body{visibility:hidden}</style>" \
                   "     <style amp-custom>" \
                   "         h1 {" \
                   "              margin: 1rem;" \
                   "            }" \
                   "      </style>" \
                   "   </head>" \
                   "        <body>" \
                   "         <h1>This is the AMP Html Body of my message</h1>" \
                   "        </body>" \
                   "</html>"

message.from_email_address = EmailAddress("from@example.com")
message.reply_to_email_address = EmailAddress("replyto@example.com")


# Adding To Recipients
# ==========================
# Add EmailAddresses using a list
to_recipients = [
    EmailAddress("recipient1@example.com"),
    EmailAddress("recipient2@example.com", "Recipient #2")
]
message.to_email_address = to_recipients

# Add EmailAddresses using the add_to_email_address function
message.add_to_email_address(EmailAddress("recipient3@example.com", "Recipient #3"))
message.add_to_email_address("recipient4@example.com")
message.add_to_email_address("recipient5@example.com", "Recipient #5")


# Adding CC Recipients
# ==========================
# Add EmailAddresses using a list
cc_recipients = [
    EmailAddress("recipient6@example.com"),
    EmailAddress("recipient7@example.com", "Recipient #7")
]
message.cc_email_address = cc_recipients

# Add EmailAddresses using the add_cc_email_address function
message.add_cc_email_address(EmailAddress("recipient8@example.com", "Recipient #8"))
message.add_cc_email_address("recipient9@example.com")
message.add_cc_email_address("recipient10@example.com", "Recipient #10")


# Adding BCC Recipients
# ==========================
# Add EmailAddresses using a list
bcc_recipients = [
    EmailAddress("recipient11@example.com"),
    EmailAddress("recipient12@example.com", "Recipient #12")
]
message.bcc_email_address = bcc_recipients

# Add EmailAddresses using the add_bcc_email_address function
message.add_bcc_email_address(EmailAddress("recipient13@example.com", "Recipient #13"))
message.add_bcc_email_address("recipient14@example.com")
message.add_bcc_email_address("recipient15@example.com", "Recipient #15")


# Adding Attachments
# ==========================
# Add Attachment directly to the list
attachments = [
    Attachment("bus.png", "image/png", "../img/bus.png")
]
message.attachments = attachments

# Add Attachment using the add_attachment function
attachment2 = Attachment("bus2", "image/png", "../img/bus.png")
attachment2.content_id = "bus"
message.add_attachment(attachment2)

# Add Attachment a filePath {string} to the array
message.add_attachment(Attachment(file_path="../html/SimpleEmail.html"))

# Add Attachment using bytes of the file
with open("../img/bus.png", 'rb') as f:
    data = f.read()
    f.close()
attachment4 = Attachment("yellow-bus.png", "image/png", content=data)

# Add CustomHeaders to Attachment
attachment4.custom_headers.append(CustomHeader("Color", "Yellow"))
attachment4.add_custom_header("Place", "Beach")

message.add_attachment(attachment4)

# Adding Custom Headers
# ==========================
# Add CustomHeader using a list

headers = [
    CustomHeader("example-type", "basic-send-complex-example"),
    CustomHeader("message-contains", "attachments, headers")
]
message.custom_headers = headers

# Add CustomHeader directly to the list
message.custom_headers.append(CustomHeader("message-has-attachments", "true"))

# Add CustomHeader using the add_custom_header function
message.add_custom_header("testMessageHeader", "I am a message header")

# Adding Metadata
# ==========================
# Add Metadata using a list

metadata = [
    Metadata("example-type", "basic-send-complex-example"),
    Metadata("message-contains", "attachments, headers")
]
message.metadata = metadata

# Add Metadata directly to the list
message.metadata.append(Metadata("message-has-attachments", "true"))

# Add Metadata using the add_metadata function
message.add_metadata("testMessageHeader", "I am metadata")

# Adding Tags
# ==========================
# Add Metadata using a list

tags = [
    "example-type:basic-send-complex-example"
]
message.tags = tags

# Add Metadata directly to the list
message.tags.append("message-has-attachments:true")

# Add Metadata using the add_metadata function
message.add_tag("I am a test message")
message.add_tag("python-Example")

# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))
