import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("MASTODON_ACCESS_TOKEN")
api_base_url = os.getenv("MASTODON_INSTANCE")

# Read text from a file
file_path = 'texts/IMG_4072.JPG.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Create a new status (tweet) with content warning and description
status = "Wikihow Museum, Meme"
description = text
cw_status = text

# Upload the image first
image_path = 'images/IMG_4072.JPG'
image_headers = {
    'Authorization': f'Bearer {access_token}'
}
image_files = {'file': ('images/IMG_4071.JPG.txt', open(image_path, 'rb'))}
image_response = requests.post(f'{api_base_url}/api/v1/media', headers=image_headers, files=image_files)
image_data = json.loads(image_response.content)
media_id = image_data.get('id')

# Create the status payload
status_payload = {
    'status': cw_status,
    'media_ids': [media_id],
    'sensitive': True,
    'spoiler_text': status,
    'visibility': 'public',  # Set the visibility as needed
    'description': description
}

# Post the status
status_headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
status_response = requests.post(f'{api_base_url}/api/v1/statuses', headers=status_headers, data=json.dumps(status_payload))

if status_response.status_code == 200:
    print("Status posted successfully!")
else:
    print("Failed to post status:", status_response.content)
