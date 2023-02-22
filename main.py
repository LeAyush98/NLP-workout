import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv("./.env")
TOKEN = os.getenv("TOKEN")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

URL_NLP = "https://trackapi.nutritionix.com"
URL_SHEET = "https://api.sheety.co/515c8dde0411d2116707dbb91f6d6964/myWorkout/workouts"

header_NLP = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

header = {
    "Authorization": TOKEN
}

add_workout = True

while add_workout:
    workout = input("Do you want to add a workout? ")
    if workout.casefold() == "yes":
        date = datetime.datetime.now()
        date = date.strftime("%d/%m/%Y")
        time = datetime.datetime.now()
        time = time.strftime("%H:%M:%S")
        payload = {
            "query":input("Please describe your workout ok "),
            "gender":"male",
            "weight_kg":60,
            "height_cm":165,
            "age":24
        }

        response = requests.post(url=f"{URL_NLP}/v2/natural/exercise", json=payload, headers=header_NLP)

        data = response.json()

        duration = int(data["exercises"][0]["duration_min"])
        exercise = data["exercises"][0]["name"]
        calories = int(data["exercises"][0]["nf_calories"])
        workout = {
        "workout" : 
            {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
            }
        
        }

        add_row = requests.post(url=URL_SHEET, json= workout, headers= header)
    else:
        add_workout = False    




