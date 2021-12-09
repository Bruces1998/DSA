import random

li = [' ',2,3,1,4,6,7,5,8]
# random.shuffle(li)
# goal state
soln = [1,2,3,4,5,6,7,8,' ']
hue = []

for i in soln:
    idx1 = li.index(i)
    idx2 = soln.index(i)
    hue.append(abs(idx1-idx2))

# print(li)
# print(soln)
# print(hue)

def hueristic(li,soln,hue,li_dup):
    hue_new = []
    for i in soln:
        idx1 = li.index(i)
        idx2 = soln.index(i)
        hue_new.append(abs(idx1 - idx2))
    hue = hue_new
    display(li)
    print('\nNumber wise Heurestic Values: ',end='')
    return hue,li


def display(li):
    print("---- ---- ---")
    print("|",li[0],"|",end=" ")
    print(li[1],"|",end=" ")
    print(li[2],"|")
    print("---- ---- ---")
    print("|",li[3],"|",end=" ")
    print(li[4],"|",end=" ")
    print(li[5],"|")
    print("---- ---- ---")
    print("|",li[6],"|",end=" ")
    print(li[7],"|",end=" ")
    print(li[8],"|")

def swap_up(li):
    li[index_blank], li[index_blank - 3] = li[index_blank - 3], li[index_blank]
    return li
def swap_down(li):
    li[index_blank], li[index_blank + 3] = li[index_blank + 3], li[index_blank]
    return li
def swap_left(li):
    li[index_blank], li[index_blank - 1] = li[index_blank - 1], li[index_blank]
    return li
def swap_right(li):
    li[index_blank], li[index_blank + 1] = li[index_blank + 1], li[index_blank]
    return li

display(li)

while li!=soln:
    index_blank = li.index(' ')
    if index_blank == 3 or index_blank == 5:
        ch = int(input("1.Swap with Up\t2.Swap with Down\t3.Swap Sideway\n"))
        li_dup = li.copy()
        if ch==1:
            li = swap_up(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        elif ch==2:
            li = swap_down(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        elif ch==3:
            if index_blank==3:
                li = swap_right(li)
                hue,li = hueristic(li, soln, hue, li_dup)
            if index_blank==5:
                li = swap_left(li)
                hue,li = hueristic(li,soln,hue,li_dup)
        else:
            print("Incorrect Choice")
            slidin
    elif index_blank == 1 or index_blank == 7:
        li_dup = li.copy()
        if index_blank==1:
            ch = int(input("1.Swap with Up\t2.Swap with Left\t3.Swap with Right\n"))
        elif index_blank==7:
            ch = int(input("1.Swap with Down\t2.Swap with Left\t3.Swap with Right\n"))
        if ch==1:
            if index_blank == 1:
                li = swap_down(li)
            elif index_blank == 7:
                li = swap_up(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        elif ch==2:
            li = swap_left(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        elif ch==3:
            li = swap_right(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        else:
            print("Incorrect Choice")

    elif index_blank==0 or index_blank==2:
        li_dup = li.copy()
        ch = int(input("1.Swap with Down\t2.Swap with Side\n"))
        if ch==1:
            li = swap_down(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        elif ch==2:
            if index_blank==0:
                li = swap_right(li)
                hue,li = hueristic(li,soln,hue,li_dup)
            elif index_blank==2:
                li = swap_left(li)
                hue,li = hueristic(li, soln, hue, li_dup)
        else:
            print("Incorrect Choice")

    elif index_blank==8 or index_blank==6:
        li_dup = li.copy()
        ch = int(input("1.Swap with Up\t2.Swap with Side\n"))
        if ch==1:
            li = swap_up(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        elif ch==2:
            if index_blank==6:
                li = swap_right(li)
                hue,li = hueristic(li,soln,hue,li_dup)
            elif index_blank==8:
                li = swap_left(li)
                hue,li = hueristic(li,soln,hue,li_dup)
        else:
            print("Incorrect Choice")

    elif index_blank==4:
        li_dup = li.copy()
        ch = int(input("1.Swap with Up\t2.Swap with Down\t3.Swap with Left\t4.Swap with Right\n"))
        if ch==1:
            li = swap_up(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        elif ch==2:
            li = swap_down(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        elif ch==3:
            li = swap_left(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        elif ch==4:
            li = swap_right(li)
            hue,li = hueristic(li,soln,hue,li_dup)
        else:
            print("Incorrect Choice")
    print(hue)

print("-------------------------------------")
print("Congrats,You won!")
print("-------------------------------------")
