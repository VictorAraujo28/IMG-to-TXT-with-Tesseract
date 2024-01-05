import pytesseract
from PIL import Image
import xml.etree.ElementTree as ET
import os

caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

# Set the path to the directory containing your images
images_directory = r"C:\Users\paulo\OneDrive\Documentos\PAGINAS"

# Loop through all files in the directory
for i in range(1, 101):
    # Construct the image file path with the correct syntax
    image_path = f'{images_directory}\\pagina{i}.jpg'

    try:
        # Open the image using Pillow
        imagem = Image.open(image_path)

        # Ask Tesseract to extract text from the image
        texto = pytesseract.image_to_string(imagem)

        # Create the root element of the XML tree
        root = ET.Element("page")
        root.set("number", str(i))
        root.text = texto

        # Create an ElementTree object and write it to an XML file
        tree = ET.ElementTree(root)
        xml_file_path = f'C:\\Users\\paulo\\OneDrive\\Documentos\\output_{i}.xml'
        tree.write(xml_file_path)

        print(f'XML file created at: {xml_file_path}')

    except Exception as e:
        print(f'Error processing pagina{i}.jpg: {e}\n')