import os
import PyPDF2

# Define the input and output folders
input_folder = r"C:\Users\Asus\Documents\Programming_Projects\my2pdf2csv\pdf_files"
output_folder = r"C:\Users\Asus\Documents\Programming_Projects\my2pdf2csv\txt_files"

# Function to extract text from a PDFvenv\Scripts\Activate.ps1
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

# Loop through the PDFs in the input folder
for root, _, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.pdf'):
            pdf_path = os.path.join(root, file)
            # Extract text from the PDF
            text = extract_text_from_pdf(pdf_path)
            # Save the extracted text to a TXT file in the output folder
            txt_filename = file.replace('.pdf', '.txt')
            txt_path = os.path.join(output_folder, txt_filename)
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)