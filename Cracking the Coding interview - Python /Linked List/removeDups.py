class ListNode:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        node = ListNode(data)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def getData(self):
        return self.getData
    
    def getNext(self):
        return self.next
    
    def setData(self,newData):
        self.data = newData

    def print_linkedList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
    
    def removeDupsTempBuffer(self):
        prev = None
        current = self.head
        seen = []
        while current:
            if current.data in seen:
                prev.next = current.next
                current = current.next
            else:
                seen.append(current.data)
                prev = current
                current = current.next
                
         
        


ll = LinkedList()
ll.add(10)
ll.add(0)
ll.add(9)
ll.add(10)
ll.add(1)

ll.print_linkedList()
ll.removeDupsTempBuffer()
print 'After removing duplicates'
ll.print_linkedList()