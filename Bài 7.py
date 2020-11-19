# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:08:36 2020

@author: Trần Thị Diệu Hiền
"""
import random
print("Nhập ngẫu nhiên số phần tử trong list")
n=int(input("Nhập n="))
T=[random.randrange(n) for i in range(n)]
print("List ngẫu nhiên là",T)
m=100000
m=int(m)
i=1
i=int(i)
while i<n:
    if m>T[i]:
        m=T[i]
    i+=1
print("Giá trị nhỏ nhất là",m)
