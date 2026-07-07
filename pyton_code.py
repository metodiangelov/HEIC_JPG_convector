from pathlib import Path
from PIL import Image
import pillow_heif

# Enable HEIC support
pillow_heif.register_heif_opener()

# Ask for the file path
input_path = input("Enter the full path to the HEIC file: ").strip().strip('"')

input_file = Path(input_path)

# Check if the file exists
if not input_file.exists():
    print("❌ File not found!")
    exit()

# Create output filename (e.g. IMG_6869_jpg.jpg)
output_file = input_file.with_name(f"{input_file.stem}_jpg.jpg")

try:
    img = Image.open(input_file)
    img = img.convert("RGB")
    img.save(output_file, "JPEG", quality=95)

    print("\n✅ Conversion successful!")
    print(f"Saved as:\n{output_file}")

except Exception as e:
    print(f"\n❌ Error: {e}")
