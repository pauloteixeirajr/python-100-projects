# Sending emails with Python using SMTP
# SMTP = Simple Mail Transfer Protocol
from smtplib import SMTP

my_email = "[EMAIL_ADDRESS]"
password = "[PASSWORD]"

with SMTP("smtp.gmail.com") as connection:
    # TLS = Transport Layer Security
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="[TO_EMAIL_ADDRESS]",
        msg="Subject: Python Mail\n\nHello, this is an email from Python"
    )
