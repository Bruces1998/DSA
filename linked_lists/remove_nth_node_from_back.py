def remove(head, n):
    start = Node()
    start.next = head
    slow = start
    fast = start

    for i in range(1, n+1):
        fast = fast.next

    while fast.next != None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return start.next

