def detec_cycle(head):
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow ==fast:
            break

    if fast== None or fast.next == None:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow