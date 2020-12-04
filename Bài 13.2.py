# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:12:27 2020

@author:Trần Thị Diệu Hiền
"""

import os.path
#Nhập tên thư mục và tên tập tin từ bàn phím
t=input("Tên thư mục là: ")
h = input("Tên file là: ")
path = 'C:\\Users\\DUC-PC\\'
os.chdir(path)
os.mkdir(t) #Tạo thư mục mới đã nhập
path1= path + t
os.chdir(path1) 
f= open(h,'w')#Tạo tập tin đã nhập vào thư mục mới đã nhập


    

