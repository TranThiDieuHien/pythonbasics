# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:29:13 2020

@author: Trần Thị Diệu Hiền
"""

import string,random
R=dict()
n=random.randrange(1,10)
T=random.choice(string.ascii_uppercase)
H=T+''.join(random.choice(string.ascii_lowercase) for i in range(n-1))
R['name']=H
A=random.randrange(1,100)
R['age']=A
print(R)