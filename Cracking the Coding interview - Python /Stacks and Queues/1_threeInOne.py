class ThreeStack:

    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (self.numstacks * stacksize)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
    
    def push(self, item, stacknum):
        if self.isFull(stacknum):
            raise Exception('Stack is Full')
        self.sizes[stacknum] += 1
        self.array[self.indexOfTop(stacknum)] = item
    
    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack is Empty')

    def isEmpty(self,stacknum):
        return self.sizes[stacknum] == 0
    
    def isFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def indexOfTop(self,stacknum):
        offset = stacknum * self.stacksize
        return offset + self.stacksize -1

    