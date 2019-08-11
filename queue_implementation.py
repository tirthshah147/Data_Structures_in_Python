class Element:
    def __init__(self,value):
        self.value = value
        self.next = None
    def change(self):
        self.value = self.value + 1
    def get(self):
        print(self.value)
        
class Queue:
    def __init__(self):
        self.storage = [None,None]
        
        

    def enqueue(self, new_element):
        if (self.storage[0] == None or self.storage[1] == None):
            self.storage[0] = new_element
            self.storage[1]= new_element
            
        self.storage[1].next = new_element
        self.storage[1] = new_element

    def peek(self):
        return self.storage[0].value

    def dequeue(self):
        temp = self.storage[0]
        self.storage[0] = self.storage[0].next
        return temp.value
        
    def changes(self,new_element):
        new_element.value = new_element.value + 1
    

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)



q = Queue()
q.enqueue(e1)
q.enqueue(e2)
q.enqueue(e3)

print (q.peek())
print (q.dequeue())

# Test enqueue
q.enqueue(e4)
# Should be 2
print (q.dequeue())
# Should be 3
print (q.dequeue())
# Should be 4
print (q.dequeue())
q.enqueue(e5)
# Should be 5
print (q.peek())