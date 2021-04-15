# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 08:27:24 2021

@author: DELL
"""

import numpy as np
import math

class project01:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
           
    def tinh_gttb(self, m1):
        j = 0
        for i in m1:
            j = j + i    
        return j/ len(m1)    
            
    
    def GTTB(self):
        gtm1 = self.tinh_gttb(self.m1)
        gtm2 = self.tinh_gttb(self.m2)
        tb = (gtm1 + gtm2)/2
        return gtm1, gtm2, tb
    
    
    def tinh_mode(self, m1):
        gt_max = (0,0)
        bienthe = 0
        for i in m1:
            bienthe = bienthe + 1
            if bienthe > gt_max[0]:
                gt_max = (bienthe, i)
        return gt_max[1]
    
    
    def mode(self):
        md1 = self.tinh_mode(self.m1)
        md2 = self.tinh_mode(self.m2)
        return md1, md2
    
    
    def tinh_phuongsai(self, m1):
        gttb1 = self.tinh_gttb(self.m1)
        tong = 0
        for i in m1:
            gt = i - gttb1
            tong = tong + (gt - gttb1)**2
        ps = tong/ len(m1)
        return ps
    
    def phuongsai(self):
        return self.tinh_phuongsai(self.m1), self.tinh_phuongsai(self.m2)
    
    
    def tinh_std(self, m1):
        std1 = self.tinh_phuongsai(m1)
        do_lech_chuan = math.sqrt(std1)
        return do_lech_chuan
    
    def std(self):
        return self.tinh_std(self.m1), self.tinh_std(self.m2)
        
    pass
    

m1 = np.array([0, 1, 2, 2])
m2 = np.array([1, 2, 3, 1])
pj = project01(m1, m2)
print(pj.GTTB())
print(pj.mode())
print(pj.phuongsai())   
print(pj.std()) 
   
    



