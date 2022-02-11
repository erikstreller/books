# send_email.py

import os
import smtplib

# get sender email adress and password from environment variables
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")


def send_email(subject: str, body: str) -> None:

    # connect to gmails mailserver and use smt port number
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        # identify
        smtp.ehlo()
        # encrypt trafic
        smtp.starttls()
        # reidentify as encrypted connection
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # type: ignore

        message: str = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)  # type: ignore


if __name__ == "__main__":
    subject = "Sunday meeting."
    body = "Talk about custom design and planing phase."

    send_email(subject, body)
