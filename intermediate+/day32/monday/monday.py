# Send a motivational quote via email on Mondays
import datetime as dt
import random
import smtplib

curr_day = dt.datetime.now().weekday()

if curr_day == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="USER", password="PASSWORD")
        connection.sendmail(
            from_addr="USER",
            to_addrs="TO_ANOTHER_USER",
            msg=f"Subject: Monday Motivation\n\n{random_quote}"
        )
