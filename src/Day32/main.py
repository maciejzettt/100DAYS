import pandas
import smtplib as sl
import os.path
import datetime as dt
from random import randint
##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

DIR = os.path.dirname(__file__)

birthdays_raw = pandas.read_csv(os.path.join(DIR, "birthdays.csv"))
birthdays = birthdays_raw.to_dict(orient="records")
print(birthdays_raw)
print(birthdays)

today_day = dt.date.today().day
today_month = dt.date.today().month

for person in birthdays:
    if int(person.get("day")) == today_day and \
        int(person.get("month")) == today_month:
        letter_file = f"letter_{randint(1,3)}.txt"
        print(f"Letter {letter_file} will be sent to {person.get('name')}.")
        with open(os.path.join(DIR, f"letter_templates/{letter_file}")) as f:
            birthday_wishes = f.read()
            birthday_wishes = birthday_wishes.replace("[NAME]", person.get("name"))
            
        with sl.SMTP_SSL("smtp.poczta.onet.pl") as email:
            print("Established")
            email.login("xxx", "yyy")
            print("Logged in")
            message = f"""Subject: Happy birthday!
            \n\n
            {birthday_wishes}
            """
            print(message)
            email.sendmail(msg= message, from_addr="xxx", to_addrs=person.get("email"))
            print("Sent")
    else:
        print(f"{person.get('name')} does not have birthday today.")