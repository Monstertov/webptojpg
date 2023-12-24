# Monstertov WebP to JPG converter
# Requirements: Pillow (pip install pillow)
from PIL import Image
import sys
import os

def webptojpg(webp_path):
    try:
        image = Image.open(webp_path)
        jpg_path = os.path.splitext(webp_path)[0] + ".jpg"
        image.convert("RGB").save(jpg_path, "JPEG")

        print(f"Conversion successful. JPG file saved at: {jpg_path}")
    except Exception as e:
        print(f"Error converting WebP to JPG: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python webptojpg.py <webp_file_path>")
    else:
        webp_file_path = sys.argv[1]
        webptojpg(webp_file_path)
