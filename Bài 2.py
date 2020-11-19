# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:04:03 2020

@author: Trần Thị Diệu Hiền
"""
#Trần Thị Diệu Hiền
#Giải PTBN lặp n lần
h=int(input("Nhập số lần lặp h= "))
#Giải PTBN bằng câu lệnh while
while h>0:
    a=float(input("Nhập a="))
    b=float(input("Nhập b="))
    if a!=0:
        if b==0:
            print("PT có nghiệm duy nhất x=0")
        else:
            print("PT có nghiệm duy nhất x=",-b/a)
    else:
        if b==0:
            print("PT có vô số nghiệm!")
        else:
            print("PT vô nghiệm!")
    h-=1
    print("Kết thúc vòng lặp while!")
#Giải PTBN bằng câu lệnh for
for i in range(h):
    a=float(input("Nhập a="))
    b=float(input("Nhập b="))
    if a!=0:
        if b==0:
            print("PT có nghiệm duy nhất x=0")
        else:
            print("PT có nghiệm duy nhất x=",-b/a)
    else:
        if b==0:
            print("PT có vô số nghiệm!")
        else:
            print("PT vô nghiệm!")
    print("Kết thúc vòng lặp For")
    
