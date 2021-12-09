def interl(A, B, C):
    if not A and not B and not C:
        return 1
    if C=="":
        return 0
    if A=="" or B=="":
        return 0

    
    first = 0
    sec = 0

    if (A[0]==C[0]):
        first = interl(A[1:], B, C[1:])

    if (B[0] == C[0]):
        sec = interl(A, B[1:], C[1:])
    print(first, sec)
    return (first or sec)

print(interl("aa", "aa", "aaaa"))
