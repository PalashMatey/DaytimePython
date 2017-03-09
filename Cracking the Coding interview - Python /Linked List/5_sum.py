#given two linked lists find the sum
#The linked lists can be variable length

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
    
def sumLinkedList(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    ll = LinkedList()
    carry = 0
    sum = 0
    while l1 or l2:
        sum = l1.data + l2.data + carry
        carry = sum / 10
        ll.add(sum%10)
        l1 = l1.next
        l2 = l2.next
    if carry:
        ll.add(carry)
    return ll


l1 = LinkedList()
l2 = LinkedList()
l1.add(8)
l1.add(1)
l1.add(7)
print 'first List', l1.print_linkedList()
l2.add(2)
l2.add(9)
l2.add(5)
print '\nSecond List',l2.print_linkedList()

ll3 = sumLinkedList(l1.head,l2.head)
print ll3.print_linkedList()

