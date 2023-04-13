# python-pdf-extractor-library-benchmarking
A simple benchmarking of PDF extractor library in Python based on how accurate they extract text from the PDF.

# About the project
There are many pdf extractor libraries for Python out there with all their pros and cons. Choosing one from many can feels numbing. We can go to google and search "the best python library for extracting pdf" and get various results. But then it is back to your need. What exactly you need? You need to extract the informations from the PDF. And it usually the text information. But what's the best extracting library to choose? Here I propose a way to benchmarking the libraries: by checking the accuracy of words extracted from the PDF source. 

# The methodology
I'm testing two python libraries for this benchmarking project: [PyMuPDF](https://github.com/pymupdf/PyMuPDF) and [PyPDF](https://github.com/py-pdf/pypdf). As for April 2023 when I post this project to Github, both projects are quite actively maintained. For both libraries I created two separated python files to extract information from PDF. The results are two text file with their respective names.

For the source used in this project I'm using an e-book freely accessed from Project Gutenberg named ["A History of Rome to 565 A. D"](https://www.gutenberg.org/files/32624/32624-pdf.pdf). I'm extracting only chapter one (from page 23 to page 26) from this source. 

For benchmarking I'm using textblob library to check each word from the text files and count how much the words that are misspelled. After getting the count I calculate the accuracy (how much the words are spelled correctly) from all words extracted.
