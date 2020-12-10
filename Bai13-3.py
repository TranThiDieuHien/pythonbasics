# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:34:44 2020

@author: Trần Thị Diệu Hiền
"""

#os.path.getsize(path): láy file size
import os,random
import string

path='C:\\Users\\DUC-PC\\' 
os.chdir(path)
file_name = 'Tentaptin'
n=int(input("Nhập tổng số lượng file với dung lượng 1MB-1024MB: ")) #vì 1MB=>1024KB nên số lượng file nằm từ khoảng 2->1048 files
i=1
for i in range(n+1):
    path1 = path + 'Baitap13'
    os.chdir(path1)
    for c in range(i+1):
        c=str(c)
        f=open(file_name + c + '.txt','w+')
        f.seek(1024*1000-1)
        f.write(random.choice(string.ascii_lowercase))
    

