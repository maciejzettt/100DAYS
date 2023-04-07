import smtplib as sl
import os.path as op

DIR = op.dirname(__file__)

with open(op.join (DIR, "email.pwd")) as pwd_f:
    email_srv = pwd_f.readline().strip()
    email_addr = pwd_f.readline().strip()
    email_pass = pwd_f.readline().strip()
print("Password retrieved")

email_connection = sl.SMTP_SSL(host=email_srv, port=465)
print("Created.")
# email_connection.starttls()
# print("Connected.")
email_connection.login(user= email_addr, password=email_pass)
print("Logged in.")
email_connection.sendmail(from_addr=email_addr, to_addrs="maciejzettt@proton.me",
                          msg="Subject: A test development message\n\nThis is a test email from smtplib. It works!")
print("Sent.")
email_connection.close()