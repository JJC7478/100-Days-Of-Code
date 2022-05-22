import smtplib
import datetime as dt
import pandas
import random

info = pandas.read_csv("Birthday-Wisher/birthdays.csv")

names = info["name"].to_list()
birthdates = []
for name in names:
    birth_year = int(info.year[info["name"] == name])
    birth_month = int(info.month[info["name"] == name])
    birth_day = int(info.day[info["name"] == name])
    birthdates.append((birth_month, birth_day,birth_year))


now = dt.datetime.now()
year = now.year
day = now.day
month = now.month

template1 = "Birthday-Wisher/letter_templates/letter_1.txt"
template2 = "Birthday-Wisher/letter_templates/letter_2.txt"
template3 = "Birthday-Wisher/letter_templates/letter_3.txt"

templates = [template1, template2, template3]

current_date = (month, day, year)
test_email = "tomagoman72@gmail.com"
my_password = "alttomago16969.!"

if current_date in birthdates:
    name = info["name"][info.month == month][info.day == day][info.year == year].to_string(index=False)
    email = info["email"][info.name == name].to_string(index=False)

    with open(random.choice(templates), mode="a+") as letter:
        letter.seek(0)
        txt = letter.read()
        letter_to_name = txt.replace("[NAME]", name)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=test_email, password=my_password)
        connection.sendmail(from_addr=test_email, to_addrs=email, msg=f"Subject:Happy Birthday\n\n{letter_to_name}")


    

    
    
