# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:52:00 2020

@author: DUC-PC
"""

#Trần Thị Diệu Hiền
#Giải chương trình bậc nhất h lần

def GiaiPTBN():
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
    GiaiPTBN()
#Giải bằng câu lệnh for
h=int(input("Nhập số lần lặp h= "))
for i in range(h):
    GiaiPTBN()
print("Kết thúc vòng lặp For")
#Giải bằng câu lệnh while
while h>0:
    GiaiPTBN()
    h-=1
print("Kết thúc vòng lặp While")


