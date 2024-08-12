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

# import fitz  # PyMuPDF
# import os

# def extract_images_from_pdf(pdf_path, output_folder):
#     # Ensure the output folder exists
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # Open the PDF
#     pdf_document = fitz.open(pdf_path)
    
#     # Iterate through pages
#     for page_number in range(len(pdf_document)):
#         page = pdf_document.load_page(page_number)
#         images = page.get_images(full=True)
        
#         for img_index, img in enumerate(images):
#             xref = img[0]
#             base_image = pdf_document.extract_image(xref)
#             image_bytes = base_image["image"]
#             image_extension = base_image["ext"]
#             image_filename = f"page_{page_number + 1}_img_{img_index + 1}.{image_extension}"
#             image_filepath = os.path.join(output_folder, image_filename)
            
#             # Save the image
#             with open(image_filepath, "wb") as image_file:
#                 image_file.write(image_bytes)
            
#             print(f"Saved image: {image_filename}")


# output_folder = 'images'

# extract_images_from_pdf(pdf_path, output_folder)
import re

def clean_text(text):
    # Remove multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text)
    # Remove non-ASCII characters (optional)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # Additional cleaning steps can be added here
    return text.strip()

cleaned_text = clean_text(text)
print(cleaned_text[:500])  # Print the first 500 characters of cleaned text


