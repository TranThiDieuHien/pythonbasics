# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:02:22 2020

@author: Trần Thị Diệu Hiền
"""


        import os, random
import string

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def random_string(length):
    letters = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
    return ''.join(random.choice(letters) for i in range(length))

don_vi = 1048576 #1kb tinh theo byte
size = don_vi * float(input('Nhập dung lượng dữ liệu giới hạn là 1MB <= size <= 1024MB: '))
t=input("Tên thư mục là: ")
h = input("Tên file là: ")
path = 'C:\\Users\\DELL\\Documents\\'
os.chdir(path)
os.mkdir(t) #Tạo thư mục mới đã nhập
path1= path + t
os.chdir(path1)
for i in range(int(size/1048576)+1):
    if float(get_size(path1)) <= size-1024*1000:
        i = str(i)
        f = open(h + i + '.txt','w+')
        f.write(random_string(1024*1000))
        f.close()
    else:
        i = str(i)
        f = open(h + i + '.txt','w+')
        f.write(random_string(int(size)-get_size(path1)))
        f.close()
