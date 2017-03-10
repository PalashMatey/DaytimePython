class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        value = self.items[len(self.items)-1]
        del self.items[len(self.items)-1]
        return value
            
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.pop()

print s.peek()

s.pop()

print s.peek()