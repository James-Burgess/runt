import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import re
from os import getenv


def run(email):
    with open("tasks/do_not_reply/email.html") as html:
        msg_html = html.read()

    sender = getenv("EMAIL_SENDER")
    msg = MIMEText(msg_html, "html")
    msg["Subject"] = "You have been blacklisted"
    msg["From"] = formataddr((str(Header("Do Not Reply", "utf-8")), sender))
    msg["To"] = email

    server = smtplib.SMTP_SSL("smtp.zoho.com", 465)
    server.login(getenv("EMAIL_USER"), getenv("EMAIL_PASS"))
    print("sending email")
    server.sendmail(sender,[email], msg.as_string())
    print("mail sent!")
    server.quit()
    return "complete"
