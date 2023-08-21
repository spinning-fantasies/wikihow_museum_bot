import os
from PIL import Image
import pytesseract

folder_path = './images/'
# print(folder_path)

# List all files in the folder
files = os.listdir(folder_path)

# Filter out subdirectories and list only files
file_list = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]

# Print the list of files
for file in file_list:
    # print(file)
    text = pytesseract.image_to_string(Image.open(f"{folder_path}{file}"))
    # print(text)
    
    # Path to the text file where you want to save the transcribed text
    output_text_file = f'./texts/{file}.txt'
    
    # Write the transcribed text to the text file
    with open(output_text_file, 'w') as textfile:
        textfile.write(text)
    
    print('OCR completed. Transcribed text saved to:', output_text_file)

