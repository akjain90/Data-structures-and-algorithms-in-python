# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:04:41 2018

@author: akjai
"""
from linked_list import linked_list
from element import element
from stacks import stack


def main():
    e0= element(0)
    e1 = element(1)
    e2 = element(2)
    e3 = element(3)
    e4 = element(4)
    e5 = element(5)
    #Linked list check 
#    ll = linked_list(e1)
#    ll.append(e2)
#    ll.append(e3)
#    ll.append(e5)
       
#    print(ll.get_position(3).value)
#    ll.insert(e4,3)
#    print(ll.get_position(3).value)
#    print(ll.get_position(4).value)
#    ll.insert(e0,0)
#    print(ll.get_position(0).value)
#    print(ll.get_position(1).value)
#    print()
#    print()
#    ll.delete(3)
#    print(ll.get_position(3).value)
#    print(ll.get_position(4).value)
#    ll.delete(0)
#    print(ll.get_position(0).value)
    
    #stack check
    ss = stack(e0)
    ss.push(e1)
    ss.push(e2)
    print(ss.pop())
    print(ss.pop())
    
if __name__=="__main__":
    main()
    