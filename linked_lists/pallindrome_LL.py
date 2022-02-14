def reverseLL(node):
    prev = None
    while node:
        curr = node
        node = node.next
        
        curr.next = prev
        prev = curr
        
    return prev


def isPalindrome(head: Optional[ListNode]) -> bool:
    
    if head == None or head.next == None:
        return True
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    slow.next = reverseLL(slow.next)
    slow = slow.next
    dummy = head
    
    while slow:
        if slow.val != dummy.val:
            return False
        
        slow = slow.next
        dummy = dummy.next
        
    return True
    
        
        