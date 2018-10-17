# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 18:38:58 2018

@author: akjai
"""

from element import element
from linked_list import linked_list

class stack:
    def __init__(self, top=None):
        self.ll = linked_list(top)
        
    def push(self, new_element):
        current = self.ll.head
        while current.next:
            current = current.next
        current.next = new_element
    
    def pop(self):
        current = self.ll.head
        position = 0
        while current.next:
            current = current.next
            position +=1
        value = current.value
        if position!=0:
            self.ll.get_position(position-1).next=None
        else:
            self.ll.head = None
        return value
        