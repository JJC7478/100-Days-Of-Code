import requests
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

#TODO Using the Nutritionix "Natural Language for Exercise" API Documentation, 
# figure out how to print the exercise stats for a plain text input.

endpoint = "https://trackapi.nutritionix.com/v2"
exercise_endpoint = f"{endpoint}/natural/exercise/"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": "ran 3 miles",
    "gender": "male",
    "weight_kg": 104,
    "height_cm": 175,
    "age": 21
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

