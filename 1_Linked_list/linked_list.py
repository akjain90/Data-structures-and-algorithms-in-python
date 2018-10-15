import element

class linked_list:
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self,position=0):
        current = self.head
        while position!=0:
            current = current.next
            position-=1
        return current
    
    def insert(self,new_element,position):
        current = self.get_position(position)
        new_element.next = current
        if position!=0:
            previous = self.get_position(position-1)
            previous.next = new_element
        else:
            self.head = new_element
            
    def delete(self, value):
        current = self.head
        position = 0
        while value!=current.value:
            current = current.next
            position+=1
        if position==0:
            self.head = self.head.next
        else:
            self.get_position(position-1).next = self.get_position(position+1)
        
        