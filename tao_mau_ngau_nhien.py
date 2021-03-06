# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 23:34:39 2021

@author: Tran Thi Dieu Hien
"""

import pandas as pd
import csv
import random

file = pd.read_csv('C:\\Users\\DUC-PC\\Downloads\\DSSV.csv')
print(file.head(10))
print("-"*50)
#Chọn ngẫu nhiên 7 sv trong ds
files = file.sample(n=7)
#Lưu vào file csv mới tên DSSVmoi.csv
files.to_csv(r'C:\\Users\\DUC-PC\\Downloads\\DSSVmoi.csv', index = None, header=True)
print(files)
