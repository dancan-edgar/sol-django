import os
import smtplib
import ssl
from django.contrib import messages
from email.message import EmailMessage


# Function to send emails
def send_emails(request, subject, body):
    email_sender = 'info@dancanedgar.com'
    email_password = os.environ.get('EMAIL_PASSWORD')
    email_receiver = 'info@dancanedgar.com'

    msg = EmailMessage()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.set_content(body)

    cxt = ssl.create_default_context()

    with smtplib.SMTP_SSL('dancanedgar.com', 465, context=cxt) as smtp:
        try:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
            messages.add_message(request, messages.INFO, 'Message sent successfully')
        except:
            messages.add_message(request, messages.ERROR, 'Message sending failed')