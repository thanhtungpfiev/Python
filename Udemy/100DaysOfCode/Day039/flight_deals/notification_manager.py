import os
import smtplib

EMAIL = "cuongphong2508@gmail.com"
PASSWORD = os.getenv('PASSWORD')


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                                msg=f"Subject:Flight ticket\n\n{message}")
