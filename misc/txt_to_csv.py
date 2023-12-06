import os
import re
import csv

def extract_data_from_text(text, file_name):
    # Extraction of Ru phone numbers with different formats
    phone_numbers = re.findall(r'(\+7|\b8)[\s\(]*(\d{3})[\)]?\s*(\d{3})[-]?\s*(\d{2})[-]?\s*(\d{2})', text) or ['phone']

    # Convert found phone numbers to the Ru format +7 (XXX) XXX-XX-XX-XX
    formatted_phone_numbers = [
        f"+7 ({match[1]}) {match[2]}-{match[3]}-{match[4]}" if match[0] == '+7' else f"8 ({match[1]}) {match[2]}-{match[3]}-{match[4]}"
        for match in phone_numbers
    ]

    # Extracting names in the Ru format 
    names = re.findall(r'\b[А-Я][а-я]+\s[А-Я][а-я]+(?:\s[А-Я][а-я]+)?', text) or ['name']

    # Extracting e-mails 
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text) or ['email']

    # Getting a file name without extension 
    file_name_without_extension = os.path.splitext(file_name)[0]

    return formatted_phone_numbers, names, emails, file_name_without_extension

def process_files(input_folder, output_folder):
    csv_file_path = os.path.join(output_folder, 'extracted_data.csv')

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Phone Number', 'Name', 'Email', 'File Name'])

        for file_name in os.listdir(input_folder):
            file_path = os.path.join(input_folder, file_name)

            if file_name.endswith('.txt') and os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    phone_numbers, names, emails, file_name = extract_data_from_text(text, file_name)

                    # Writing data to a CSV file 
                    for data in zip(phone_numbers, names, emails, [file_name] * len(phone_numbers)):
                        csv_writer.writerow(data)

if __name__ == "__main__":
    # Absolute address of the project 
    script_path = os.path.abspath(__file__)
    
    # Absolute address of the "txt_files" folder 
    input_folder = os.path.abspath(os.path.join(script_path, '..', '..', 'txt_files'))
    
    # Absolute address of the "csv_files" folder 
    output_folder = os.path.abspath(os.path.join(script_path, '..', '..', 'csv_files'))
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    process_files(input_folder, output_folder)
