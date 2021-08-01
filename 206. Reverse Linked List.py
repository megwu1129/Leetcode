# iteration
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
      
      
      
# recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.helper(head, None)
    
    def helper(self, curr, prev):
        if curr is None:
            return prev
        n = curr.next
        curr.next = prev
        return self.helper(n, curr)
