# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:17:16 2020

@author: Trần Thị Diệu Hiền
"""

import random
n=int(input("Nhập n= "))
R=[random.randrange(n) for i in range(n)]
print("List ngẫu nhiên là",R)
M=0
M=int(M)
i=0
i=int(i)
while i<n:
    if M<R[i]:
        M=R[i]
    i+=1       
print("Giá trị lớn nhất là",M)
   
    
    
    

    
    

   