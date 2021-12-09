def ins(source, x):
    n = len(source)
    res = []
    # print(source,x)
    for i in range(n//2 + 1):
        p1 = source[:i]
        p2 = source[i:]
        res.append(p1 + x + p2)


    return res

def parens(n):
    if n==0:
        return [""]

    words = parens(n-1)
    print(words)
    result = []
    for word in words:
        # print(word)
        result += ins(word, "()")


    return list(set(result))

a = parens(4)
print(a)
