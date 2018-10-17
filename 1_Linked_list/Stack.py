# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 00:14:15 2018

@author: akjai
"""
from LinkedList import LinkedList

class Stack:
    def __init__(self, head):
        self.ll = LinkedList(head)
        
    def push(self, new_elem):
        self.ll.append(new_elem)
        
    """Edit this function based on the head critarion"""
    def pop(self):
        current = self.ll.head
        position = 0 
        while current.next!=None:
            current = current.next
            position+=1
        previous = self.ll.get_position(position-1)
        temp = current.value
        previous.next=None
        return(temp)
        