# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:50:45 2020

@author: DUC-PC
"""

import csv
with open('Data.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['STT','Ten','Tuoi'])
    writer.writerow(['1', 'Thang','18'])
    writer.writerow(['2', 'Thang','24'])
    writer.writerow(['3','Hien','18'])
    writer.writerow(['4','Dan','56'])
    writer.writerow(['5','Do','12'])
    writer.writerow(['6','Duc','24'])
    writer.writerow(['7','Duong','48'])
    writer.writerow(['8','Loc','47'])
    writer.writerow(['9', 'Phong', '18'])
    writer.writerow(['10', 'Ngan','19'])
    writer.writerow(['11', 'Lam','23'])
    writer.writerow(['12', 'Quan', '18'])
    writer.writerow(['13', 'Buu','18'])
    writer.writerow(['14', 'Tham', '19'])
    
import pandas
result = pandas.read_csv('Data.csv')
print(result)