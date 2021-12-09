def solve(A):
    i = 0
    j = len(A) - 1

    while( i <= j):
        print(i, j, A[i], A[j])


        if A[i]==A[j]:
            i+=1
            j-=1

        else:
            i+=1

            if j!=len(A) - 1:
                j = len(A) - 1


    if(j!=len(A)-1):
        return i-len(A)+j+1


    return i - 1


print(solve("oqycntornscygodzdctxnhoc"))
