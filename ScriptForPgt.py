#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 04:53:02 2020

@author: snowden
"""

import pdftables_api


c.csv('/home/snowden/Downloads/1034-DEPENSES-2016.pdf', 'pgt-depenses-2016.csv') 
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML
i = 0
listOfPDF = ['', '']

for file in listOfPDF:
    i += 1
    c = pdftables_api.Client('83ile2qas3u3')
    c.csv((file, 'file-{}' ).format(i))
