# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:34:03 2018

@author: akjai
"""

from LinkedList import LinkedList
from Queue import Queue
from Element import Element
from Stack import Stack
from RingBuffer import RingBuffer

def main():
#    e0 = Element(0)
#    e1 = Element(1)
#    e2 = Element(2)
#    e3 = Element(3)
    rb = RingBuffer(4)
    rb.append(0)
    rb.append(1)
    rb.append(2)
    rb.append(3)
    rb.append(4)
    rb.append(5)
    print(rb.delete())
    print(rb.delete())
    print(rb.get_data())
    
if __name__=="__main__":
    main()