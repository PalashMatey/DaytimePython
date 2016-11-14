
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = self.head
        while (current is not None):
            next_new = current.next
            current.next = prev
            prev = current
            current = next_new
        self.head = prev         
        
    def add(self,data):
        node = ListNode(data)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
             

    def getData(self):
        return self.val
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.val = newdata
    
    def gotoLast(self):
        count = 0;
    
    def print_list(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
        


mylist = Solution()

mylist.add(1)
mylist.add(2)
mylist.add(3)
print "The list"
mylist.print_list()

print 
mylist.reverseList()
print "Reversed List"
mylist.print_list()