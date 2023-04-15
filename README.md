# python-pdf-extractor-library-benchmarking
A simple benchmarking of PDF extractor library in Python based on how accurate they extract text from the PDF.

# About the project
There are many pdf extractor libraries for Python out there with all their pros and cons. Choosing one from many can feels numbing. We can go to google and search "the best python library for extracting pdf" and get various results. But then it is back to your need. What exactly you need? You need to extract the informations from the PDF. And it usually the text information. But what's the best extracting library to choose? Here I propose a way to benchmarking the libraries: by checking the accuracy of words extracted from the PDF source. 

# Libraries 
Python libraries I used for this project are:
1. [PyPDF](https://github.com/py-pdf/pypdf)
2. [PDFMiner](https://github.com/pdfminer/pdfminer.six)
3. [PyMuPDF](https://github.com/pymupdf/PyMuPDF)
4. [Textblob](https://github.com/sloria/TextBlob)
5. Pandas

# Sources
All e-books I'm using for benchmarking these libraries collected from Project Gutenberg.
1. [A History of Rome to 565 A. D. by Arthur E. R. Boak](https://www.gutenberg.org/ebooks/32624)
2. [Days of Heaven Upon Earth by A. B. Simpson](https://www.gutenberg.org/ebooks/28416)
3. [Hidden Symbolism of Alchemy and the Occult Arts by Herbert Silberer](https://www.gutenberg.org/ebooks/27755)
4. [Tempest and Sunshine by Mary Jane Holmes](https://www.gutenberg.org/ebooks/17260)
5. [The Samurai Strategy by Thomas Hoover](https://www.gutenberg.org/ebooks/34323)

# How I did the benchmarking
I extract ten pages from each sources using PyPDF, PDFMiner, and PyMuPDF. I made a class to feed in each libraries result to Textblob and check whether the words are correct of misspelled. I count the misspelled and using the number to calculate the accuracy of each libraries for each sources.
