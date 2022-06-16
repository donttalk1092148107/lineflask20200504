#https://github.com/UB-Mannheim/tesseract/wiki
import pytesseract
from PIL import Image
image = Image.open(r'photo.jpeg')
code = pytesseract.image_to_string(image)
print(code)
