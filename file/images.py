# Takes a image file as a command line argument using sys.argv, 
# opens it with Pillow, 
# converts it to grayscale, and saves it as output.jpg 
# — handle missing argument and invalid file with sys.exit()

import sys
from PIL import Image

def main():
    if len(sys.argv) != 2:
        print("Usage: python images.py <image_file>")
        sys.exit()

    image_file = sys.argv[1]

    try:
        # Open the image file
        img = Image.open(image_file)
        
        # Convert the image to grayscale
        gray_img = img.convert("L")
        
        # Save the grayscale image as output.jpg
        gray_img.save("output.jpg")
        print("Image converted to grayscale and saved as output.jpg")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

if __name__ == "__main__":
    main()