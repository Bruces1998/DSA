'''
The below technique uses
two pointers to find the middle
of the linked list. It is known
as the Runner Technique.
'''
def getMid(node):
    slow = node
    fast = node

    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next

    return slow