import os
import PyPDF2

# Absolute address of the project 
script_path: str = os.path.abspath(__file__)

# Absolute address of the "txt_files" folder 
input_folder: str = os.path.abspath(os.path.join(script_path, '..', '..', 'pdf_files'))

# Absolute address of the "csv_files" folder 
output_folder: str = os.path.abspath(os.path.join(script_path, '..', '..', 'txt_files'))

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text: str = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

# Loop through the PDFs in the input folder
for root, _, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.pdf'):
            pdf_path: str = os.path.join(root, file)
            # Extract text from the PDF
            text: str = extract_text_from_pdf(pdf_path)
            # Save the extracted text to a TXT file in the output folder
            txt_filename: str = file.replace('.pdf', '.txt')
            txt_path: str = os.path.join(output_folder, txt_filename)
            with open(txt_path, 'w', encoding = 'utf-8') as txt_file:
                txt_file.write(text)