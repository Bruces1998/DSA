from sys import stdin
def pairSum(arr, n, num) :
    if len(set(arr))==1:
        if arr[0]==num//2:
            return ((n-1)*n//2)
    arr.sort()

    c = 0
    i = 0
    j = n-1
    while i < j:
        if arr[i]+arr[j] == num:
            c1 = 1
            c2 = 1
            t1 = arr[i]
            t2 = arr[j]
            while i<n-1 and i<j and t1==arr[i+1]:
                c1 += 1
                i += 1
           
            while j>-1 and i<j and t2==arr[j-1]:
                c2 += 1
                j -= 1
            i+=1
            j-=1
            c += c1 * c2
                
        elif arr[i]+arr[j] > num:
            j -= 1
        else:
            i += 1
    
    return c
        

def tripletSum(arr, n, num):
    arr.sort()
    s = 0
    d = set(arr)
    for i in range(n-1):
        s+=pairSum(arr[i+1:],n-i-1,num-arr[i])
        
            
    return s