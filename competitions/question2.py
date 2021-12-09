t = int(input())
A = []
B = []
C = []
for _ in range(t):
    a, b, c = list(map(int, input().split(" ")))
    A.append(a)
    B.append(b)
    C.append(c)
    
def get_opposite(a, b, c):
    diff = abs(a-b)
    circum = 2*diff
    
    if a > circum or b > circum:
        return -1
    
    if circum < c:
        return -1
    if c > diff:
        return c - diff
    return c+diff

for i in range(t):
    print(get_opposite(A[i], B[i], C[i]))
    