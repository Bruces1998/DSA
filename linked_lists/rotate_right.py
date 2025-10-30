'''
Rotate a linkedlist to the right k steps
'''

def rotate_linkedlist(head, k):
    if head == None or head.next == None or k == 0:
        return head
    
    temp = head
    length = 1

    while temp.next != None:
        temp = temp.next
        length += 1

    shifts = length - k
    temp = head
    while shifts != 0:
        temp = temp.next
        temp -= 1

    head = temp.next
    temp.next = None

    return head
    