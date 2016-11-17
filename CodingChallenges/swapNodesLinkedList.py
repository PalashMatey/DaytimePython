# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = self
        prev.next = head
        while prev.next and prev.next.next:
            prev.next, prev.next.next, prev.next.next.next = prev.next.next, prev.next, prev.next.next.next
            prev = prev.next.next
        return self.next
        