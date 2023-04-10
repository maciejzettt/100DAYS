import smtplib as sl
import os.path as op
import runpy
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent

commonFunctions = runpy.run_path(op.join(PROJECT_ROOT, "commonFunctions.py"))

credentials = commonFunctions['email_credentials']()
print("Password retrieved")

email_connection = sl.SMTP_SSL(host=credentials["server"], port=465)
print("Created.")
# email_connection.starttls()
# print("Connected.")
email_connection.login(user=credentials["user"], password=credentials["password"])
print("Logged in.")
email_connection.sendmail(from_addr=credentials["user"], to_addrs="maciejzettt@proton.me",
                          msg="Subject: A test development message\n\nThis is a test email from smtplib. It works!")
print("Sent.")
email_connection.close()