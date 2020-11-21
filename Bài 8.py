# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:19:48 2020

@author: DUC-PC
"""
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("dieuhientran1907@gmail.com","nanamiharuka123456789")
msg = "Hello friends"
for i in range(5):
    if i<5:
        server.sendmail("dieuhientran1907@gmail.com","nanamiharuka111@gmail.com",msg)
        i+=1
server.quit()
 