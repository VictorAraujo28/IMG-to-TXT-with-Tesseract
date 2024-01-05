import pytesseract
from PIL import Image

# Step one: read the image
image_path = "C:\\Users\\paulo\\OneDrive\\Documentos\\PAGINAS\\pagina2.jpg"
caminho = r"C:\Program Files\Tesseract-OCR"

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

# Open the image using Pillow
imagem = Image.open(image_path)

# Step two: ask Tesseract to extract text from the image
texto = pytesseract.image_to_string(imagem)
print(texto)