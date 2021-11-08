import os
import smtplib
from secure import password
from email.message import EmailMessage

EMAIL_ADDRESS = 'your_email_here@example.com'
EMAIL_PASSWORD = password

message = EmailMessage()
message['Subject'] = 'Subject here'
message['From'] = 'from@example.com'
message['To'] = 'to@example.com'
message.set_content('Here is the message.')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(message)