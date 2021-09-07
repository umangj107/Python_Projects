from twilio.rest import Client
import smtplib

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"

# DETAILS FOR MAIL NOTIFICATION
TO_EMAIL = "ENTER DESTINATION EMAIL ADDRESS"
FROM_EMAIL = "ENTER YOUR SOURCE EMAIL ADDRESS"

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body = message,
            from_= TWILIO_VIRTUAL_NUMBER,
            to = TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("YOUR EMAIL", "YOUR PASSWORD")
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject:New Low Price Alert!\n\n{message}".encode('utf-8')
            )