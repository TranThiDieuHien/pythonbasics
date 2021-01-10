# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 00:11:38 2020

@author: DUC-PC
"""

import csv

with open('writeData.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #way to write to csv file
    writer.writerow(['Class', 'Name', 'Age'])
    writer.writerow(['B1', 'Hien','18'])
    writer.writerow(['B2', 'Buu','18'])
    writer.writerow(['B3', 'Tham', '19'])
    writer.writerow(['B1', 'Tram','17'])
    writer.writerow(['B2', 'Duy','20'])
    writer.writerow(['B3', 'Phong', '18'])
    writer.writerow(['B1', 'Thang','18'])
    writer.writerow(['B2', 'Thang','24'])
    writer.writerow(['B3', 'Minh', '20'])
    writer.writerow(['B1', 'Phuoc','21'])
    writer.writerow(['B2', 'Ngan','19'])
    writer.writerow(['B3', 'Toan', '22'])
    writer.writerow(['B1', 'Thanh','21'])
    writer.writerow(['B2', 'Lam','23'])
    writer.writerow(['B3', 'Quan', '18'])
import pandas
result = pandas.read_csv('writeData.csv')
print(result)