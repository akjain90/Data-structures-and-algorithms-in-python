# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 01:05:10 2018

@author: akjai
"""

class RingBuffer:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.data = [None]*buffer_size
        
    def append(self,value):
        self.data.pop(0)
        self.data.append(value)
        
    def delete(self):
        return(self.data.pop(0))
    
    def get_data(self):
        return self.data