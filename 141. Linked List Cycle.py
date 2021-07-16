class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
  
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
      
      
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = fast = head
        if fast.next is not None:
            fast = fast.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

# time: O(n)
# space: O(1)
