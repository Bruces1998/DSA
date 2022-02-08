def getLength(string):
    n = len(string)
    start = 0
    end = 0

    ans = 0
    mapp = {}

    while end < n:
        if mapp.get(string[end]) is not None and start <= mapp[string[end]]:
            start = mapp[string[end]] + 1

        else:
            maxx = max(maxx, end -start + 1)
        
        mapp[string[end]] = end

    return maxx