# MoodTunes 

## Overview
MoodTunes is a web application that generates Spotify playlists based on a combination of health data and musical preference. 

## Use cases 
Workout enhancement. Stress reduction. Recreational.
Base version may be used by anyone with a spotify account. Enhanced version required a smart watch to be used.

## Functional requirements 
- Able to authenticate a users smart watch and Spotify account and gain permission to access corresponding data
- Able to cache this authentication data for each corresponding user id so we dont need to reauthenticate
- Able to make requests to the APIs using the authentication details and retrieve this data in json format
- Parse jsons and store in relevant database tables
- Able to generate playlists based on retrieved data
- Playlists should be created directly in users Spotify account

## Non functional requirements
Reauthentication may need to be performed after a certain timeframe
Optionally health data may be retrieved reguarly e.g. hourly 

## Technical requirements
Each database should have a composite primary key of user_id + datetime 
Input should be validated 

