import os
import requests
import datetime
import time
from dotenv import load_dotenv

load_dotenv()


# Mastodon API endpoint and access token
access_token = os.getenv("MASTODON_ACCESS_TOKEN")
api_base_url = os.getenv("MASTODON_INSTANCE")

# Construct headers with authorization
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

# Make the request to schedule the status
response = requests.get(f'{api_base_url}/api/v1/scheduled_statuses/', headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print('Error scheduling status:', response.status_code)
    print(response.text)
