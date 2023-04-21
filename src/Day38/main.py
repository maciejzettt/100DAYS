import requests
import api_auth
import print_dict
import datetime as dt

NUTRI_ENDP = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_hdr = {
    "x-app-id": api_auth.NUTRI_APPID,
    "x-app-key": api_auth.NUTRI_APIKEY,
    "Content-Type": "application/json"
}

nutri_post = {
    "query":"ran 3 miles",
    "gender":"male",
    "weight_kg":95,
    "height_cm":176,
    "age":30
}

exercise = input("Describe your exercise: ")
nutri_post['query'] = exercise

print("Waiting for response...")
nutri_response = requests.post(url=NUTRI_ENDP, headers=nutri_hdr, json=nutri_post)
nutri_response.raise_for_status()
exercise_data = nutri_response.json().get("exercises")
exercise_data = exercise_data[0]
print_dict.print_dict(exercise_data)

sheety_hdr = {
    "Authorization": "Bearer ffJdsjL73nsklkNKD93kdqp"
}

now = dt.datetime.now()
sheety_post = {
    "workout": {
        "date": dt.datetime.strftime(now, "%d/%m/%Y"),
        "time": dt.datetime.strftime(now, "%H:%M:%S"),
        "exercise": str(exercise_data.get("name")).title(),
        "duration": str(exercise_data.get("duration_min")),
        "calories": str(exercise_data.get("nf_calories"))
    }
}

print("Posting data to the spreadsheet...")
sheety_response = requests.post(url=api_auth.SHEETY_URL, headers=sheety_hdr, json=sheety_post)
sheety_response.raise_for_status()
print(f"Data posted; http status: {sheety_response.status_code}")
