import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

pdf_path = 'anatomy_vol_1.pdf'
text = extract_text_from_pdf(pdf_path)
print(text[:500])  # Print the first 500 characters to check

from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def extract_images_from_pdf(pdf_path, output_folder):
    images = convert_from_path(pdf_path)
    image_texts = []
    
    for i, image in enumerate(images):
        image.save(f'{output_folder}/page_{i}.png', 'PNG')
        
        # Optional: OCR to extract text from images (if tables are in image format)
        text = pytesseract.image_to_string(image)
        image_texts.append(text)
    
    return image_texts


output_folder = r'D:\Sakthi\College\Semester 5\chatmed\chatmed'
image_texts = extract_images_from_pdf(pdf_path, output_folder)
print(image_texts[0])  # Check OCR result for the first image

