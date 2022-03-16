def solve(self, A):
    if len(A) == 1:
        return 1
    low = -1
    
    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            low = A[i-1]
            
        if A[i] < low:
            return 0
            
    return 1