from pypdf import PdfReader

filesource = r'from project Gutenberg 32624-pdf.pdf'

reader = PdfReader(filesource)

text_list = []

for page in range(23, 26):
    pagetext = reader.pages[page]
    text = pagetext.extract_text()
    text_list.append(text)

all_text = ' '.join(text_list)

with open(r'from_guttenberg_pypdf.txt', 'w', encoding = 'utf-8') as file:
    file.write(all_text)