'''
Program to reverse linked list
iteratively.
'''

def reverse(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr

    return prev

'''
Program to reverse linked list
recursively.
'''

def reverse(node, prev = None):
    if not node:
        return prev
    
    next = node.next
    node.next = prev

    return reverse(next, node)