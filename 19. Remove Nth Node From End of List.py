# Two pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        curr = head
        length = 0
        while curr is not None:
            curr = curr.next
            length+=1
        
        curr = dummy
        for i in range(length-n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
      
# One pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        for i in range(n):
            fast = fast.next
        if fast is None: # if we are delecting head
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
