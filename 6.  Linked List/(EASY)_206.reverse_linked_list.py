# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class IterativeSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        curr, prev = head, None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

# December 28th, 2025