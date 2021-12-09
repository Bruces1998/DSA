def multiply_strings(A, B):
    m = len(A)
    n = len(B)
    memo = [0 for _ in range(m+n)]

    for i in range(m-1,-1, -1):
        for j in range(n - 1, -1, -1):
            mul = (ord(A[i]) - ord('0')) * (ord(B[j]) - ord('0'))
            sum = memo[i + j + 1] + mul
            memo[i + j] += sum // 10
            memo[i + j + 1] = sum % 10
    ans = ''
    for val in memo:
        if val!=0 or len(ans)!=0:
            ans+=str(val)
    return ans


print(multiply_strings('321', '23'))
