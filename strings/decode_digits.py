def decode(s, n):
    if n == 0 or n == 1:
        return 1
    
    count = 0
    if s[n-1] != "0":
        count = decode(s, n-1)

    if s[n-2] == "1" or (s[n-2] == "2" and s[n-1] < "7"):
        count += decode(s, n-2)

    return count

print(decode("1234", 4))