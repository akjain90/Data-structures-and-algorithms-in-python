# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:32:43 2018

@author: akjai
"""

class LinkedList:
    def __init__(self,head=None):
        self.head = head
        
    def append(self,new_elem):
        current = self.head
        while current.next!=None:
            current = current.next
        current.next = new_elem
    
    def get_position(self,position):
        current = self.head
        while position!=0:
            current = current.next
            position-=1
        return(current)
        
    def insert(self,new_elem,position):
        current = self.get_position(position)
        if position!=0:
            previous = self.get_position(position-1)
            new_elem.next = current
            previous.next = new_elem
        else:
            new_elem.next = self.head
            self.head = new_elem
            
    def delete_position(self,position):
        current = self.get_position(position)
        if position!=0:
            previous = self.get_position(position-1)
            previous.next = current.next
        else:
            self.head = self.head.next
        
    def delete_val(self,value):
        current = self.head
        exist = 1
        position = 0
        while (current.value!=value):
            current = current.next
            position+=1
            if current.next == None:
                exist = 0
                print("No element")
                break
        if (exist):
            if position!=0:
                previous = self.get_position(position-1)
                previous.next = current.next
            else:
                self.head = self.head.next
