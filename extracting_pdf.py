import os
import pytesseract
import fitz
from PIL import Image
from pdfminer import high_level
from pypdf import PdfReader
from sys import argv

"""
How to use:
> Just type this into your CLI:
    python extracting_file.py <source> <result> <start> <end>

    <source>: PDF file name and location you want to extract, including the ".pdf".
    <result>: text file name for extracting result, including the ".txt".
    <start>: Starting page you want the extraction tobegin.
    <end>: Ending page you want the extraction to stop.
"""

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # change this with where you put tesseract.exe in your system

def pymu(pdf, start, stop):
    """Extracting PDF text using PyMuPDF."""
    # open PDF
    pdf_open = fitz.open(pdf)
    # create image from PDF page(s)
    for page_index in range(start - 1, stop):
        page = pdf_open[page_index]
        image_info = page.get_pixmap().pil_save(f"{page_index}.png", optimize = True, dpi = (600, 600))  
        print(f'{page_index}.png is saved')
    image_list = [f'{i}.png' for i in range(start - 1, stop)]
    print("Tesseract process...")
    
    # Read text from image list and append them into a list
    image_text = []
    for image in image_list:
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        image_text.append(text)
        print(f'{image} text is appended.')
    
    # Delete images
    for img in image_list:
        print(f'Deleting {img}.')
        os.remove(img)

    # Join all texts in the list as a single text file.
    return ' '.join(image_text)


def pdf_miner(pdf, start, stop):
    """Extracting PDF text using PDFMiner."""
    text_list = []
    for i in range(start - 1, stop):
        text = high_level.extract_text(pdf, page_numbers = [i])
        text_list.append(text)
    alltext = '\n'.join(text_list)
    return alltext
    

def py_pdf(pdf, start, stop):
    """Extracting PDF file using PyPDF."""
    reader = PdfReader(pdf)
    text_list = []
    for page in range(start - 1, stop):
        pagetext = reader.pages[page]
        text = pagetext.extract_text()
        text_list.append(text)
    all_text = ' '.join(text_list)
    return all_text

if __name__ == "__main__":
    pdf_file = argv[1]
    start_page = int(argv[3])
    end_page = int(argv[4])

    text_pymu = pymu(pdf_file, start_page, end_page)
    text_pypdf = py_pdf(pdf_file, start_page, end_page)
    text_pdfminer = pdf_miner(pdf_file, start_page, end_page)

    with open(f'pymupdf_{argv[2]}.txt', 'w', encoding = 'utf-8') as mp:
        mp.write(text_pymu)
        print("> Done writing for PyMuPDF.")
    
    with open(f'pdfminer_{argv[2]}', 'w', encoding = 'utf-8') as m:
        m.write(text_pdfminer)
        print("> Done writing for PDFMiner.")

    with open(f'pypdf_{argv[2]}', 'w', encoding = 'utf-8') as pp:
        pp.write(text_pypdf)
        print("> Done writing for PyPDF.")

    
    