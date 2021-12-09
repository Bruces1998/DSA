
def ins(source, x):
    n = len(source)
    res = []
    # print(source,x)
    for i in range(n+1):
        p1 = source[:i]
        p2 = source[i:]
        res.append(p1 + x + p2)


    return res
def dups(string,n):
    if n<0:
        return [""]

    words = dups(string,n-1)
    wo = string[n]

    result = []
    for word in words:
        result+=ins(word, wo)

    return set(result)

print(dups("aabc",3))
