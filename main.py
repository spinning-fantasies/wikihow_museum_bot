import os
import requests
import json
import pytesseract
from PIL import Image, ImageFile
from dotenv import load_dotenv
import datetime
import timedelta


load_dotenv()

access_token = os.getenv("MASTODON_ACCESS_TOKEN")
api_base_url = os.getenv("MASTODON_INSTANCE")

ImageFile.LOAD_TRUNCATED_IMAGES = True

folder_path = './temp_images/'

# List all files in the folder
files = os.listdir(folder_path)

# Filter out subdirectories and list only files
file_list = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]

# Print the list of files
for file in file_list:
    text = pytesseract.image_to_string(Image.open(f"{folder_path}{file}"))
    print(text)
    
    # Path to the text file where you want to save the transcribed text
    output_text_folder = './temp_texts/' 
    output_text_file = f'{output_text_folder}{file}.txt'
    
    # Create the destination folder if it doesn't exist
    if not os.path.exists(output_text_folder):
        os.makedirs(output_text_folder)

    # Upload the image first
    image_path = f'{folder_path}{file}'
    image_headers = {
    'Authorization': f'Bearer {access_token}'
    }

    image_files = {'file': (f'temp_images/{file}', open(image_path, 'rb'))}
    image_response = requests.post(f'{api_base_url}/api/v1/media', headers=image_headers, files=image_files)
    print(image_response)
    image_data = json.loads(image_response.content)
    media_id = image_data.get('id')

    # print(media_id)

    # Set schedule 
    current_time = datetime.datetime.now()
    interval = datetime.timedelta(hours=6)
    scheduled_time = current_time + interval
    print(scheduled_time)

    # Create a new status (tweet) with content warning and description
    status = "Wikihow Museum, Meme"
    description = text
    cw_status = text

    # Create the status payload
    status_payload = {
        'status': cw_status + "#WikihowMuseum",
        'media_ids': [media_id],
        'sensitive': True,
        'spoiler_text': status,
        'visibility': 'public',  # Set the visibility as needed
        'description': description,
        'scheduled_at': scheduled_time.isoformat()
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
    else:
        print("Failed to post status:", status_response.content)
