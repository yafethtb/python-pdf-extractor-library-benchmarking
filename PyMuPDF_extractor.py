import pytesseract
import fitz
from PIL import Image
from sys import argv

# argv[1] = PDF file name.
# argv[2] = TXT file name.
# argv[3] = start page.
# argv[4] = stop page.

# Uncomment the comment below and enter the location where you place tesseract.exe in your system to pytesseract.pytesseract.tesseract_cmd
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
# This might be different if you use non-Windows OS. I don't know, I'm using Windows while making this.

def pdf_extractor(pdf_file, start, stop):
    '''Open and extract pdf file. It will create PNG images in the process. You can delete them after all the process done.'''
    pdf_open  = fitz.open(pdf_file)
    
    # This step turn argument inputs from string to integer
    start = int(start)
    stop = int(stop)

    # Change PDF pages into PNG images.
    for page_index in range(start - 1, stop):
        page = pdf_open[page_index]
        image_info = page.get_pixmap().pil_save(f"{page_index}.png", optimize = True, dpi = (600, 600))  
        print(f'{page_index}.png is saved')

    # Listing all image names created
    image_list = [f'{i}.png' for i in range(start - 1, stop)]

    image_text = []
    print("Tesseract process...")
    
    # Read text from image list and append them into a list
    for image in image_list:
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        image_text.append(text)
        print(f'{image} text is appended.')
    
    # Join all texts in the list as a single text file.
    return ' '.join(image_text)

if __name__ == "__main__":
    with open(argv[2], 'w') as uu:
        uu.write(pdf_extractor(argv[1], argv[3], argv[4]))

print('Process done.')
