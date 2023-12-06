# my2pdf2csv
## A small and simple utility written in Python and Batch to automate my repetitive tasks for pdf and excel work.
I created this project to automate the creation of Excel spreadsheets based on data from PDF documents. The goal was to extract a person's phone number, name and email from a PDF file full of miscellaneous information and paste it into a spreadsheet.

The project is written in Python and Batch and I used PyPDF2 as the pdf parser.

Here is what this utility can do:
* Extract text from .pdf files and write them to .txt files
* Recognise phone numbers in .txt files (Ru format only)
* Recognise names of people in .txt files
* Recognise emails in .txt files
* Extract information from .txt files and write them to .csv files

## How to use it?
Here are the simplest instructions for working with this utility.

1. Clone or download this project
2. Install Python: https://www.python.org/downloads/
3. Copy the .pdf files you need into the "pdf_files" folder
4. Run "my2pdf2csv.bat"
5. Go to the "csv_files" folder
6. Open "extracted_data.csv"
7. ???
8. Profit!!!

## Why is this utility needed if my-pdf-to-csv is available?
It's simple: I decided to make a version that works not on Xpdf, but on PyPDF2 

## Find a bug?
If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created!

## Known issues (Work in progress)
1. If there is a space in the project path, the utility will not work. 

Example:

`C:\cool_folder\my-pdf-to-csv` - the utility will work ✅

`C:\cool folder\my-pdf-to-csv` - the utility will not work ❌

2. After running the script, the old .txt and .csv files remain in the "text_files" and "csv_files" folders.
  
I recommend to clean these folders from unnecessary files for the reliability of your data in the tables.

## Did this project help you?
If you want to thank the developer for his work, give this project a star! ⭐
