def reverse(string):

    left = 0
    right = len(string)
    ans = ""
    
    while left < right:
        curr = ""
        while left < right and string[left] == " ":
            left += 1

        while left < right and string[left] != " ":
            curr += string[left]
            left += 1
        
        if curr != "":
            ans.append(curr)

    return " ".join(ans[::-1])
    