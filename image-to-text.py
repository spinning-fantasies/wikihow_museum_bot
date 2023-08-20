import os
import pytesseract
from PIL import Image

def image_to_text(image_path):
    # Load the image using Pillow (PIL)
    image = Image.open(image_path)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image)

    return text

def process_images_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out only the JPG image files
    image_files = [f for f in files if f.lower().endswith('.jpg')]

    for image_file in image_files:
        # Get the file name without extension to use as the output file prefix
        file_prefix = os.path.splitext(image_file)[0]

        # Full path to the input image
        image_path = os.path.join(folder_path, image_file)

        # Convert the image to text
        extracted_text = image_to_text(image_path)

        # Output file path with the same prefix as the image but with .txt extension
        output_file_path = os.path.join(folder_path, f'{file_prefix}.txt')

        # Save the extracted text to the output file
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)

        print(f'Text extracted and saved to: {output_file_path}')

def main():
    # Input folder path (replace this with the path to your folder containing JPG images)
    folder_path = 'archive'

    # Process JPG images in the folder and extract text
    process_images_in_folder(folder_path)

if __name__ == "__main__":
    main()
