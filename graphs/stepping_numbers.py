'''
Code to demonstarte 
stepping numbers
'''
def bfs(n, m, num):

    queue = [num]
    
    while queue:
        stepnum = queue.pop(0)
        if ( stepnum in range(n, m+1)):
            print(stepnum)

        if stepnum == 0 or stepnum > m:
            continue

        lastDigit = stepnum%10
        stepnumA = stepnum*10 + (lastDigit-1)
        stepnumB = stepnum*10 + (lastDigit+1)

        if (lastDigit == 0):
            queue.append(stepnumB)

        elif lastDigit == 9:
            queue.append(stepnumA)

        else:
            queue.append(stepnumA)
            queue.append(stepnumB)

def display(n, m):

    for i in range(10):
        bfs(n, m, i)


display(1, 21)