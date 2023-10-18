import os
import shutil
from datetime import datetime

DOWNLOAD_PATH = os.path.expanduser('~/Downloads')

# File type categorization based on extensions
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.md'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
    'Other': []
}

def get_file_category(filename):
    """Return the file category based on its extension."""
    _, ext = os.path.splitext(filename)
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return 'Other'

def move_file_to_category(file_path):
    """Move the file to its appropriate category and subfolder."""
    filename = os.path.basename(file_path)
    category = get_file_category(filename)
    
    # Get the last modified month and year
    timestamp = os.path.getmtime(file_path)
    dt_obj = datetime.fromtimestamp(timestamp)
    subfolder_name = f"{dt_obj.year}{str(dt_obj.month).zfill(2)}"
    
    # Construct the target folder path
    target_folder = os.path.join(DOWNLOAD_PATH, category, subfolder_name)
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    shutil.move(file_path, os.path.join(target_folder, filename))

def main():
    # Make sure category folders exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(DOWNLOAD_PATH, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
            
    # Iterate over files in the download folder and move them
    for filename in os.listdir(DOWNLOAD_PATH):
        file_path = os.path.join(DOWNLOAD_PATH, filename)
        if os.path.isfile(file_path):
            move_file_to_category(file_path)

if __name__ == "__main__":
    main()
