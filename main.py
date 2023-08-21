import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("MASTODON_ACCESS_TOKEN")
api_base_url = 'https://3615.computer'

# upload test files to /api/v1/media
IMAGES_FILES = [
    "./IMG_4070.JPG"
]

files_root = Path("./images/")
media_ids = []
for file in IMAGES_FILES:
    test_file = files_root / file
    data = {
        'description': '#WikiHowMuseum' + file
    }
    files = {
        'file': (file, test_file.open('rb'), 'application/octet-stream')
    }
    url = "%s/api/v1/media" % (api_base_url)
    r = requests.post(url, 
        files=files, 
        headers={'Authorization': 'Bearer %s' % (access_token)})
    json_data = r.json()

    media_id = json_data['id']
    media_ids.append(media_id)

# after collecting the media ids, include them in the toot payload
data = { 
    "status": """
    - décrivez-vous en deux mots.
    - dynamique et anticapitaliste.
    
    #WikihowMuseum
    """, 
    "media_ids[]": media_ids,
    "visibility": "public"
}

url = "%s/api/v1/statuses" % (api_base_url)
r = requests.post(url, 
        data=data, 
        headers={'Authorization': 'Bearer %s' % (access_token)})
json_data = r.json()
print(json_data)