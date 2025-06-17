import pytesseract
from PIL import Image

# Path to the Tesseract executable (change this if Tesseract is installed in a different location)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the input image
image_path = 'Sample_Image.png'

try:
    # Open the image using Pillow
    image = Image.open(image_path)
except FileNotFoundError:
    print(f"Error: Image file '{image_path}' not found.")
    exit()

# Extract text from the image using Tesseract OCR
extracted_text = pytesseract.image_to_string(image)

# Display the extracted text
print("Extracted Text:\n")
print(extracted_text)

# Save the extracted text to a file
output_file = "Sample_Output.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(extracted_text)

print(f"\nText successfully saved to '{output_file}'")
