memo = {}
def lcs(A, B):
    if not A or not B:
        return 0
    if (A, B) not in memo:

        if A[0]==B[0]:
            memo[(A, B)] =  1 + lcs(A[1:], B[1:])
        else:

            memo[(A, B)] = max(lcs(A[1:], B), lcs(A, B[1:]))

    return memo[(A, B)]

print(lcs("aniket", "anit"))
