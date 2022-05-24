import requests
from datetime import datetime
import smtplib
import time

TEST_EMAIL = "tomagoman72@gmail.com"
PASSWORD = "This is my password"
EMAIL_TEXT = "Subject:Look up\n\nThe ISS is above you!"
MY_LAT = 34.061970
MY_LNG = -118.441540


parameters = {
    "formatted": 0
}

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_data = iss_response.json()
iss_lat = float(iss_data["iss_position"]["latitude"])
iss_lng = float(iss_data["iss_position"]["longitude"])

sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()

sun_data = sun_response.json()
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
now_hour = time_now.hour

while True:
    time.sleep(60)
    if ( MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LNG - 5 <= iss_lng <= MY_LNG + 5) and (now_hour > sunset or now_hour < sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=TEST_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=TEST_EMAIL, to_addrs=TEST_EMAIL, msg=EMAIL_TEXT)






