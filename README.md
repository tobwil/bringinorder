# bringinorder

Organizes files in the `Downloads` directory into categorized folders based on their file types and the month of their last modification.

## Features

- Automatically categorizes files into: `Documents`, `Images`, `Videos`, and `Other`.
- Creates subfolders based on the month and year of the file's last modification, e.g., `202310` for October 2023.
- If the main categories or subfolders don't exist, the script will create them.

## Prerequisites

- Python 3

## Usage

1. Clone this repository:
- git clone https://github.com/tobwil/bringinorder.git
- cd bringinorder

2. Run the script:
- python3 bringinorder.py

## File Categorization

Files are categorized based on their extensions as follows:

- **Documents**: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`, `.md`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.ico`
- **Videos**: `.mp4`, `.mkv`, `.flv`, `.avi`, `.mov`, `.wmv`
- **Other**: All other file extensions.

## Contribution

Feel free to fork this repository, make changes, and open a pull request if you think your changes can improve the functionality of this script.

## License

This project is licensed under the MIT License.

## Author

[YourName](https://github.com/tobwil)


