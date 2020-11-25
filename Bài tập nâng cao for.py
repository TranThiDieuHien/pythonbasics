# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:51:02 2020

@author: Trần Thị Diệu Hiền

"""

print("Bài tập nâng cao về vòng lặp for")
list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}), 
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for (a,b) in list2:
    print(a)
    for index,x in enumerate(a):
        print("-Vị trí thứ",index,"là",x,":",a.get(x))
    print(b)
    for index,y in enumerate(b):
        print("-Vị trí thứ",index,"là",y,":",b.get(y))
        
   

        

   
      
