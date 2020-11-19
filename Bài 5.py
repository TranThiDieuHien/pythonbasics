# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:25:23 2020

@author: Tran Thi Dieu Hien
"""
import math
#Tạo một List gồm cấc số thực
x=[5,2,3,6]
#Thực hiện lặp truy xuất đến từng phần tử trong List và in giá trị của từng phần tử ra màn hình
for pt in x:
    print("Giá trị từng phần tử trong list ",pt)
#Thực hiện lặp truy xuất đến từng phần tử trong List và thực hiện tính logarith của từng phần tử và in giá trị đó ra màn hình
for i in range(len(x)):
    print("Logarit là",math.log10(x[i]))
   
    
    
