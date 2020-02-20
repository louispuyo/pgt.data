#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 08:31:46 2020

@author: snowden
"""

import PyPDF2
# pdf file object
pdf_path = '/home/snowden/Downloads/1034-DEPENSES-2016.pdf'
csv_path ='pgt-2eme.csv'
# you can find find the pdf file with complete code in below
pdfFileObj = open('/home/snowden/Downloads/1034-DEPENSES-2016.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
print(pdfReader.numPages)
# a page object

pageObj = pdfReader.getPage(0)
pageObj = pdfReader.getPage(1)

# extracting text from page.
# this will print the text you can also save that into String
print(pageObj.extractText())


import csv
import os
from miner_text_generator import extract_text_by_page
def export_as_csv(pdf_path, csv_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    counter = 1
    with open(pdf_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for page in extract_text_by_page(pdf_path):
            text = page[0:100]
            words = text.split()
            writer.writerow(words)
if __name__ == '__main__':
    pdf_path = 'w9.pdf'
    csv_path = 'w9.csv'
    export_as_csv(pdf_path, csv_path)