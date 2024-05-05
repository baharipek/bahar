# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:29:58 2024

@author: avuka
"""
import qrcode
import pyqrcode  
import png 

qrCode = pyqrcode.create(content='model.py',encoding=None)
                                                      
                                  
qrCode.png('code.txt', scale=5, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])

qrCode.show()
