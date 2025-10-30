def countSay(n):
    # Base case: if n is 1, the sequence is "1".
    if n == 1:
        return "1"
    
    prev = "1"
    i = 1

    while i !=n:
        j = 0
        count = 1
        next = ""

        # Iterate through the 'prev' string to build the 'next' one.
        while j < len(prev) - 1:
            if prev[j] == prev[j+1]:
                # If the next character is the same, increment count.
                count += 1
            else:
                # If it's different, append the count and character, then reset count.
                next += str(count) + prev[j]
                count = 1
            j+= 1

        # Append the count and character for the last group of digits.
        next += str(count) + prev[j]
        prev = next
        i += 1

    return prev
