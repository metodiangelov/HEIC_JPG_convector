HEIC to JPG Converter

This Python script converts a single HEIC image (from iPhones or other devices) into a JPG image.

Requirements

Install the required libraries:

pip install pillow pillow-heif
How to Run
Save the script as:
heic_to_jpg.py
Open Command Prompt or PowerShell.
Navigate to the folder containing the script:
cd "D:\YourFolder"
Run the script:
python heic_to_jpg.py
Enter the Image Path

When prompted:

Enter the full path to the HEIC file:

Enter the complete path to your HEIC image.

Example:

D:\Download\IMG_6869.HEIC

or

"D:\Download\IMG_6869.HEIC"

(Both with and without quotes work.)

Output

The script creates a JPG file in the same folder as the original image.

Example:

Original:
D:\Download\IMG_6869.HEIC

Output:
D:\Download\IMG_6869_jpg.jpg
Success Message

If everything works correctly, you'll see:

✅ Conversion successful!
Saved as:
D:\Download\IMG_6869_jpg.jpg
Troubleshooting

File not found

Make sure the file path is correct and that the file exists.

Missing module

If you receive an error like:

ModuleNotFoundError: No module named 'pillow_heif'

Install the required packages:

pip install pillow pillow-heif
