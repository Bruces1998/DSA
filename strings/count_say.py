def countSay(n):
    
    prev = "1"
    i = 1

    while i !=n:
        j = 1
        count = 1
        next = ""

        while j != len(prev):
            if prev[j] != prev[j-1]:
                next += str(count) + prev[j-1]

            else:
                count += 1

            j+= 1

        next += str(count) + prev[j-1]
        prev = next
        i += 1

    return prev

