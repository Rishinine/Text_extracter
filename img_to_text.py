from PIL import Image
import pytesseract
import pyperclip

# please uncomment and specify the path of tesseract if it is not set to environment variable
# pytesseract.pytesseract.tesseract_cmd = ' '

def extract_text_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    return text

# Example usage
image_path = 'sample.png'  # Update this path as needed
pyperclip.copy(extract_text_from_image(image_path=image_path))