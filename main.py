import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("MASTODON_ACCESS_TOKEN")
api_base_url = os.getenv("MASTODON_INSTANCE")

filename = 'IMG_4100'

# Read text from a file
file_path = f'texts/{filename}.JPG.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Create a new status (tweet) with content warning and description
status = "Wikihow Museum, Meme"
description = text
cw_status = text

# Upload the image first
image_path = f'images/{filename}.JPG'
image_headers = {
    'Authorization': f'Bearer {access_token}'
}
image_files = {'file': (f'images/{filename}.JPG', open(image_path, 'rb'))}
image_response = requests.post(f'{api_base_url}/api/v1/media', headers=image_headers, files=image_files)
image_data = json.loads(image_response.content)
media_id = image_data.get('id')

# Create the status payload
status_payload = {
    'status': cw_status + "#WikihowMuseum",
    'media_ids': [media_id],
    'sensitive': True,
    'spoiler_text': status,
    'visibility': 'public',  # Set the visibility as needed
    'description': description
}

print(status_payload)

# Post the status
status_headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
status_response = requests.post(f'{api_base_url}/api/v1/statuses', headers=status_headers, data=json.dumps(status_payload))

if status_response.status_code == 200:
    print("Status posted successfully!")
    
    text_source_path = f'texts/{filename}.JPG.txt'  # Replace with the actual source file path
    image_source_path = f'images/{filename}.JPG'  # Replace with the actual source file path
    destination_folder = 'posted'  # Replace with the actual destination folder path
    
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    # Construct the full path for the destination
    text_destination_path = os.path.join(destination_folder, os.path.basename(text_source_path))
    image_destination_path = os.path.join(destination_folder, os.path.basename(image_source_path))

    # Move the file to the destination
    os.rename(text_source_path, text_destination_path)
    print(f"File '{text_source_path}' moved to '{text_destination_path}'")

    os.rename(image_source_path, image_destination_path)
    print(f"File '{image_source_path}' moved to '{image_destination_path}'")

else:
    print("Failed to post status:", status_response.content)
