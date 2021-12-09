t = int(input())
inp = []
for _ in range(t):
    inp.append(int(input()))
    

def get_number(n):
    count = 0
    i = 0
    while(count < n):
        if i%3 == 0 or i%10 == 3:
            i+=1
            continue
            
        count+=1
        i+=1
        
        
    return i-1

for val in inp:
    
    print(get_number(val))
            
        
    