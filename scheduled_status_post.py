import os
import mastodon
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

# Mastodon instance URL
instance_url = os.getenv("MASTODON_INSTANCE")
# Your Mastodon access token
access_token = os.getenv("MASTODON_ACCESS_TOKEN")
# Folder containing images
image_folder = 'temp_images'

# Initialize Mastodon API
client = mastodon.Mastodon(
    access_token=access_token,
    api_base_url=instance_url
)

def post_image_with_warning(image_path, content_warning, sensitive=True):
    # Upload media
    media = client.media_post(image_path, description=content_warning, sensitive=sensitive)

    # Compose the status
    status = f"Image with content warning: {content_warning}"

    # Post the status with the uploaded media
    client.status_post(status, media_ids=[media])

    print("Image posted successfully!")

def schedule_posts():
    if not os.path.exists(image_folder):
        print("Image folder not found.")
        return

    content_warning = "Sensitive Content Warning"
    sensitive = True
    interval_hours = 12  # Interval between posts

    image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.lower().endswith(('.png', '.jpg', '.jpeg'))]

    current_time = datetime.now(timezone.utc)

    for idx, image_path in enumerate(image_paths):
        scheduled_time = current_time + timedelta(hours=idx * interval_hours)
        client.status_post(
            "Scheduled image post",
            media_ids=[client.media_post(image_path)["id"]],
            scheduled_at=scheduled_time
        )
        print(f"Image {image_path} scheduled for {scheduled_time}")

if __name__ == "__main__":
    schedule_posts()
