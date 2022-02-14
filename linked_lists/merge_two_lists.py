def mergeTwoLists(l1, l2):
    if l1 == None and l2 == None:
        return None

    if l1 == None:
        return l2
    
    if l2 == None:
        return l1

    a1 = l1
    a2 = l2

    if l1.val < l2.val:
        ans = l1
    
    else:
        ans = l2

    while(a1 != None and a2 != None):
        if a1.val <= a2.val:
            while(a1 != None and a1.val <= a2.val):
                temp = a1
                a1 = a1.next

            temp.next = a2

        else:
            while(a2 != None and a2.val < a1.val):
                temp = a2
                a2 = a2.next

            temp.next = a1
    return ans

