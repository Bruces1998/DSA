def numDecodings(s):
    if s[0]=="0":
        return {}

    if len(s)==1:
        return {s}
    ways = []


    for i in range(1, len(s)):
        p1 = s[:i]
        p2 = s[i:]

        if p2[0]=="0":
            continue

        ways.append(numDecodings(p1)+(numDecodings(p2)))

    if int(s) <=26:
        ways.append({s})
    return ways

a = numDecodings('123')
print(a)
