def get_row_col(k):
    n = int(k**(0.5))
    if k == 1:
        return (1, 1)
    num = (n-1)**2
    while(num!=k):
        row, col = 1, n
        while(row<=n):
            num+=1
            if(num == k):
                return (row, col)
            row+=1
        row-=1
        col-=1
        while(col > 0):
            num+=1
            if(num == k):
                return (row, col)
            col-=1
            

            
        n+=1
        
t = int(input())
inp = []
for _ in range(t):
    inp.append(int(input()))

for val in inp:
    ans = get_row_col(val)
    print(ans[0], ans[1])
            
