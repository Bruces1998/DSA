def getInt(headA, headB):
    if headA is None or headB is None:
        return None
    A = headA
    B = headB
    
    while(A != B):
        A = headB if A is None else A.next
        B = headA if B is None else B.next
        
            
    return A