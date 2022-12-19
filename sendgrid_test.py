
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='',
    to_emails='wiizzydreadmill@gmail.com',
    subject='WISHARE API VERIFICATION',
    html_content='<strong></strong>')
try:
    sg = SendGridAPIClient("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")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)