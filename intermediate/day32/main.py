# ABW Project
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "EMAIL"
MY_PASSWORD = "PASSWORD"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (_, row) in data.iterrows()}

if today in birthday_dict:
    person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=MY_PASSWORD)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person.email,
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
