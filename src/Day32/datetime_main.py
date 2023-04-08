import datetime as dt
import smtplib as sl
from os import path
from random import choice

DIR = path.dirname(__file__)

today = dt.date.today()
today_day_of_week = today.weekday()

if today_day_of_week == 4:
    print("It's monday - a quote will be sent!")
    with open(path.join(DIR, "quotes.txt")) as quotes_file:
        quotes = quotes_file.readlines()
        this_week_quote = choice(quotes).strip()
        print(this_week_quote)
        
    with sl.SMTP_SSL("smtp.poczta.onet.pl") as email:
        print("Established")
        email.login("xxx", "yyy")
        print("Logged in")
        message = f"""Subject: Your motivational quote
        \n\n
        This is your motivational quote for this week:
        {this_week_quote}
        """
        email.sendmail(msg= message, from_addr="xxx", to_addrs="zzz")
        print("Sent")
        
else:
    print("It's not monday")