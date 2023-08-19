from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from app.models import *

def save_activity_data():
    # 1. Read the JSON file
    with open('app/static/activityData.json', 'r') as f:
        data = json.load(f)

    # Assuming there could be multiple activity data, loop through them
    activity = data['data'][0]
    # 2. Extract the relevant values
    bpm = activity['heart_rate_data']['summary']['avg_hr_bpm']
    bmr = activity['calories_data']['BMR_calories']
    total_burned_calories = activity['calories_data']['total_burned_calories']
    timestamp = datetime.strptime(activity['metadata']['start_time'], "%Y-%m-%dT%H:%M:%S.%f+00:00")  # Convert the string to a datetime object

    # 3. Save the data to the database
    new_activity = Activity(bpm=bpm, bmr=bmr, total_burned_calories=total_burned_calories, timestamp=timestamp)
    return new_activity

def save_body_data():
    # 1. Read the JSON file
    with open('app/static/bodyData.json', 'r') as f:
        data = json.load(f)

    # Assuming there could be multiple activity data, loop through them
    body = data['data'][0]
    # 2. Extract the relevant values
    estimated_fitness_age=body['measurements_data']['measurements'][0]['estimated_fitness_age']
    blood_pressure=body['blood_pressure_data']['blood_pressure_samples'][0]['systolic_bp']
    bmi=body['measurements_data']['measurements'][0]['BMI']
    body_temperature=body['temperature_data']['body_temperature_samples'][0]['temperature_celsius']    
    timestamp = datetime.strptime(body['metadata']['start_time'], "%Y-%m-%dT%H:%M:%S.%f+00:00")  # Convert the string to a datetime object

    # 3. Save the data to the database
    new_body = Body(estimated_fitness_age=estimated_fitness_age, blood_pressure=blood_pressure, bmi=bmi, timestamp=timestamp)
    return new_body

def save_sleep_data():
    # 1. Read the JSON file
    with open('app/static/sleepData.json', 'r') as f:
        data = json.load(f)

    # Assuming there could be multiple activity data, loop through them
    sleep_data = data['data'][0]['sleep_durations_data']
    num_REM_events = sleep_data['asleep']['num_REM_events']
    num_wakeup_events = sleep_data['awake']['num_wakeup_events']
    sleep_efficiency = sleep_data['sleep_efficiency']
    timestamp = datetime.strptime(data['data'][0]['metadata']['start_time'], "%Y-%m-%dT%H:%M:%S.%f%z")

    # 3. Save the data to the database
    new_sleep = Sleep(num_REM_events=num_REM_events, num_wakeup_events=num_wakeup_events, sleep_efficiency=sleep_efficiency, timestamp=timestamp)
    return new_sleep

def load_health_data(uname):
    activityData = save_activity_data()
    bodyData = save_body_data()
    sleepData = save_sleep_data()
    user = User.query.filter_by(username=uname).first()
    new_health = Health(activity=activityData, body=bodyData, sleep=sleepData, user_id=user.id) # Directly set the related Activity object
    db.session.add(new_health)
    db.session.commit()
