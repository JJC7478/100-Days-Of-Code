import smtplib
import random
import datetime as dt

with open("quotes.txt") as file:
    lines = file.readlines()

quote_list = [line.strip() for line in lines]
quote = random.choice(quote_list)

now = dt.datetime.now()
weekday = now.weekday()

test_email = "tomagoman72@gmail.com"
my_email = "johnjonahc@gmail.com"
my_password = "this_is_my_password"

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=test_email, password=my_password)
        connection.sendmail(from_addr=test_email, to_addrs=my_email, msg=f"Subject:Hello\n\n{quote}")