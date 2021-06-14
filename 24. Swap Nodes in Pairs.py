# Recursion

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        first = head
        new_start = head.next
        
        second = first.next
        temp = second.next
        second.next = first
        
        if not temp or not temp.next:
            first.next = temp
        else:
            first.next = temp.next
            self.swapPairs(temp)
        
        return new_start
        
# Iteration
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        firstNode = head
        new_start = head.next
        
        while True:
            secondNone = firstNode.next
            # save temp's location
            temp = secondNone.next
            #swap
            secondNone.next = firstNode
            
            if temp is None or temp.next is None:
                firstNode.next = temp
                break
            
            firstNode.next = temp.next
            firstNode = temp
        
        return new_start
        
# opt - recursion
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        temp = head
        if temp and temp.next:
            temp.val,temp.next.val=temp.next.val,temp.val
            self.swapPairs(temp.next.next)
        return head
        
        
# opt - iteration
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        temp=head
        while temp is not None and temp.next is not None:
            temp.val,temp.next.val=temp.next.val,temp.val
            temp=temp.next.next
        return head
    
        
        

            
        
        
