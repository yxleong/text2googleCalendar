import os
import json
import google.auth
from googleapiclient.discovery import build
from googleapiclient import errors

# Define the text to be converted into a calendar event
text = "Meeting with team tomorrow at 2 PM"

# Define the calendar ID
calendar_id = "primary"

# Authenticate and construct the Calendar API client
creds, project = google.auth.default()
service = build('calendar', 'v3', credentials=creds)

# Extract the event details from the text
event_details = {}
event_details['summary'] = text.split(" at ")[0]
event_details['description'] = text
event_details['start'] = {'dateTime': '2023-02-09T14:00:00-07:00', 'timeZone': 'America/Los_Angeles'}
event_details['end'] = {'dateTime': '2023-02-09T15:00:00-07:00', 'timeZone': 'America/Los_Angeles'}

# Create the event
event = service.events().insert(calendarId=calendar_id, body=event_details).execute()

# Print the event details
print(f"Event created: {event['summary']} on {event['start']['dateTime']}")
