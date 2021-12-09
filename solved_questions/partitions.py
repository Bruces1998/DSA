def solve(A, B):
        count = 0
        for i in range(1, A - 1):
            for j in range(i+1, A):
                if sum(A[:i]) == sum(A[i:j]) == sum(A[j:]):
                    count+=1


        return count

solve(5, [1, 2, 3, 0, 3])
