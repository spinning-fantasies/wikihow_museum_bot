import os
import requests
import datetime
import pytz
import time
from dotenv import load_dotenv

load_dotenv()

# Mastodon API endpoint and access token
access_token = os.getenv("MASTODON_ACCESS_TOKEN")
api_base_url = os.getenv("MASTODON_INSTANCE")

# Create a session with the Mastodon API instance
session = requests.Session()
session.headers.update({'Authorization': f'Bearer {access_token}'})

# Content of the post
post_content = "Hello, this is a scheduled post in Europe/Paris timezone !"

# Convert current time to Central European Timezone (CET)
cet_timezone = pytz.timezone('Europe/Paris')  # CET is also known as Europe/Paris
current_time = datetime.datetime.now(pytz.utc)
cet_current_time = current_time.astimezone(cet_timezone)

# Calculate the scheduled time (e.g., post after 1 hour)
scheduled_time = cet_current_time + datetime.timedelta(seconds=42)

# Convert the scheduled time to UTC
scheduled_time_utc = scheduled_time.astimezone(pytz.utc)

# Prepare the data for the API request
data = {
    "status": post_content,
    "scheduled_at": scheduled_time_utc.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
}

# API endpoint for creating a scheduled status
api_url = f"{api_base_url}/api/v1/statuses"

# Make the API request to schedule the post
response = session.post(api_url, json=data)

if response.status_code == 200:
    print("Post scheduled successfully!")
else:
    print(f"Error scheduling post. Status code: {response.status_code}")
    print(response.text)

# Wait for a bit to allow the scheduled time to arrive
time.sleep(10)
