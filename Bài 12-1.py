# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:51:04 2020

@author: Trần Thị Diệu Hiền
"""

import random
n=random.randrange(50,1000)
R=random.sample(range(-1000,1000),n)
print("-List các số nguyên ngẫu nhiên trong khoảng [-1000, 1000]:",R)
T=[random.uniform(-1000.0,1000.0) for i in range(n)]
print("-List các số thực ngẫu nhiên trong khoảng [-1000.0, 1000.0]:",T)