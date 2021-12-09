#Aniket Singh 17101A0037 INFT A
j1 = 0
j2 = 0
cap1 = int(input("Set a Capacity for 1st jug: "))
cap2 = int(input("Set a Capacity for 2nd jug: "))
output = int(input("Enter Capacity Goal: "))

steps = 0
flag = 0
while (j1 != output and j2 != output):
    steps = steps + 1
    print("\nJUG 1: ",j1,"\nJUG 2:",j2,("\n"))
    print("Choose one of the following operations: \n"
          "1. Completely fill jug1\n"
          "2. Completely fill jug2\n"
          "3. Completely empty jug1\n"
          "4. Completely empty jug2\n"
          "5. Transfer all water from jug1 to jug2\n"
          "6. Transfer all water from jug2 to jug1\n"
          "7. Transfer some water from jug1 to jug2\n"
          "8. Transfer some water from jug2 to jug1\n"
          "9. Exit"
        )
    ch = int(input(""))
    if ch == 1:
        j1 = cap1
    elif ch == 2:
        j2 = cap2
    elif ch == 3:
        j1 = 0
    elif ch == 4:
        j2 = 0
    elif ch == 5:
        if (j1 + j2) <= cap2 and j1 > 0:
            j1 = 0
            j2 = j1 + j2
        else:
            print("Cannot perform this action")
    elif ch == 6:
        if (j1 + j2 )<= cap1 and j2 > 0:
            j1 = j1+j2
            j2 = 0
        else:
            print("Cannot perform this action")
    elif ch ==7:
        if j1 > 0 and (j1 + j2) > cap2:
            j1 = j1 - (cap2 - j2)
            j2 = cap2
        else:
            print("Cannot perform this action")
    elif ch ==8:
        if j2 > 0 and (j1 + j2) > cap1:
            j2 = j2 - (cap1 - j1)
            j1 = cap1
        else:
            print("Cannot perform this action")
    elif ch==9:
        flag = 1
        print("Thank you for Playing, Better Luck next Time !")
        break
    else:
        print("Invalid choice. Please Stick to the Menu")
if flag == 0:
    print("Goal achieved!")
    print("You Completed the Puzzle in",steps,"moves !")
    if (j1 == output):
        j2 = 0
    else:
        j1 = 0
    print("j1 = ", j1, "j2 =", j2)
