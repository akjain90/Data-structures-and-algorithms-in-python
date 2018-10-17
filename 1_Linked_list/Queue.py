# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 23:33:46 2018

@author: akjai
"""
from LinkedList import LinkedList

class Queue:
    def __init__(self, head):
        self.ll = LinkedList(head)
    
    def enque(self, new_elem):
        self.ll.append(new_elem)
    
    def deque(self):
        temp = self.ll.head.value
        self.ll.delete_position(0)
        return(temp)
    
    def peak(self,position=0):
        return(self.ll.get_position(position))
        