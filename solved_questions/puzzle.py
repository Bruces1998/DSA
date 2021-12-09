import random
#Genrating starting puzzle using random module in python
def calc_heuristic(puzzle, ideal):
    h=0
    for i in range(3):
        for j in range(3):

            if puzzle[i][j] == ideal[i][j]:
                h += 1
                if i==2 and j==2: #as 9 is considered as blank
                    h-=1

    return h

def get_index(puzzle, target): #to get index of target value in puzzle matrix
    for i in range(3):
        for j in range(3):
            if puzzle[i][j]==target:
                return i,j

def print_puzzle(puzzle): #to print puzzle matrix
    for i in range(3):
        print(puzzle[i][0], puzzle[i][1], puzzle[i][2])
l=[]
p=[]
while True:
    temp=random.randint(1,9) #generating random numbers between 1 to 9 using randint
    if temp not in p:
        p.append(temp)
    if len(p)==9:
        break

puzzle=[]
for i in p:
    if len(l)!=3:
        l.append(i)
    else:
        puzzle.append(l) #generating 3*3 matrix
        l=[]
        l.append(i)
puzzle.append(l)
# print(puzzle)

ideal=[[1,2,3],[4,5,6],[7,8,9]]

#9 is considered as blank
#heuristic value is number of correct positions
#max heuristic value is 8
#at every step we should be increasing heuristic value

print("Please consider value 9 as blank")
initial_heuristic=calc_heuristic(puzzle,ideal)
prev = initial_heuristic
while True:
    print_puzzle(puzzle)
    choice=int(input("Which number you want to move?? "))
    if choice>8 or choice<1:
        print("Please enter value in the range 1 to 8")
        continue
    x,y=get_index(puzzle, choice)
    blank_x, blank_y=get_index(puzzle,9)
    d1=blank_x-x if blank_x>x else x-blank_x
    d2=blank_y-y if blank_y>y else y-blank_y
    if (d1==1 and d2==1):
        print("You can't move this number :-(")
        continue
    flag=0
    if d1==1 and (d2==0 or d2==1):
        flag=1
    elif d2==1 and (d1==0 or d1==1):
        flag=1


    if flag==1:
        puzzle[x][y], puzzle[blank_x][blank_y] = puzzle[blank_x][blank_y], puzzle[x][y]
        new = calc_heuristic(puzzle, ideal)
        print("Heuristic value: ", new)
        if new < prev:
            print("You are making a wrong move :-( ")
            # puzzle[x][y], puzzle[blank_x][blank_y] = puzzle[blank_x][blank_y], puzzle[x][y]
            puzzle[blank_x][blank_y], puzzle[x][y] = puzzle[x][y], puzzle[blank_x][blank_y]
            continue
        else:
            prev=new

        if new==8:
            print("Hurray!!! You have won the game :-)")
            break

    else:
        print("You can't move this number :-(")
        continue
