def ispall(string):
    i = 0
    j = len(string) - 1
    while(i <=j):
        if string[i]!=string[j]:
            return False
        i+=1
        j-=1
    return True
def minCharsforPalindrome(A):

    # Write your code here
    i = len(A)-1
    while(i !=0 and A[0]!=A[i]):
        i-=1
            
    while i > -1:
        if A[i] == A[0] and ispall(A[:i+1]):
            return len(A) - i -1

        i -= 1
            
                
    return len(A)    3