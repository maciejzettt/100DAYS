import requests
import datetime as dt
import smtplib


from pathlib import Path
import os.path as op
import runpy
PROJECT_ROOT = Path(__file__).parent.parent.parent
COMMON_FN_DICT = runpy.run_path(op.join(PROJECT_ROOT, "commonFunctions.py"))
CREDENTIALS = COMMON_FN_DICT['email_credentials']()

Timer = COMMON_FN_DICT['RepeatedTimer']


MY_LAT = 51 # Your latitude
MY_LONG = 16.970880 # Your longitude


def is_ISS_above() -> bool:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    print(f"ISS lat: {iss_latitude}, long: {iss_longitude}")
    if iss_latitude > (MY_LAT - 5) and iss_latitude < (MY_LAT + 5) \
        and iss_longitude > (MY_LONG -5) and iss_longitude < (MY_LONG + 5):
        print("ISS above")
        return True
    else:
        print("ISS not above")
        return False


def is_dark() -> bool:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_raw = data["results"]["sunrise"].split("T")[1].split("+")[0]
    sunset_raw = data["results"]["sunset"].split("T")[1].split("+")[0]

    sunrise = dt.time.fromisoformat(sunrise_raw)
    sunset = dt.time.fromisoformat(sunset_raw)
    time_now =dt.datetime.now().time()
    print(sunset, time_now, sunrise)
    
    if sunset < time_now or time_now < sunrise:
        print("It's dark")
        return True
    else:
        print("It's light")
        return False

def loop_function() -> None:
    if is_ISS_above() and is_dark():
        print("Message will be sent: conditions met.")
        with smtplib.SMTP_SSL(CREDENTIALS['server']) as smtp_conn:
            print("Connected")
            smtp_conn.login(user=CREDENTIALS['user'], password=CREDENTIALS['password'])
            print("Logged in.")
            message = """Subject: ISS - look up! \n\n
            Look up, the International Space Station is above you and you should see it now!
            """
            smtp_conn.sendmail(from_addr=CREDENTIALS['user'], to_addrs="maciejzettt@proton.me", msg=message)
            print("Sent.")
    else:
        print("Message won't be sent: conditions not met")        
    
loop = Timer(10, loop_function)    
print("Timer initialized.")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




