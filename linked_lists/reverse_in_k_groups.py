'''
Problem Link:
https://leetcode.com/problems/reverse-nodes-in-k-group/
'''

def reverseKNodes(head, k):
    stack = []
    start = Node(0) #reference node for starting
    prev = start

    while head:
        stack.append(head)
        head = head.next

        if len(stack) == k or not head:
            while stack:
                curr = stack.pop(-1)
                curr.next = None

                prev.next = curr
                prev = prev.next

        elif not head:
            while stack:
                curr = stack.pop(0)
                curr.next = None

                prev.next = curr
                prev = prev.next

    return start.next

        
