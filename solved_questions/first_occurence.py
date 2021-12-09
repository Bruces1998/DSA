def solve(A):
        hash_table = dict()
        minn = 2**31
        for i in range(len(A)):
            if hash_table.get(A[i]):
                minn = min(minn, hash_table[A[i]])
            
            else:
                hash_table[A[i]] = i
                
            print(hash_table)
        if minn != 2**31:
            return A[minn]
        return -1


print(solve([ 8, 15, 1, 10, 5, 19, 19, 3, 5, 6, 6, 2, 8, 2, 12, 16, 3 ]))