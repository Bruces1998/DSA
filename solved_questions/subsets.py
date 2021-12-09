def getsubs(sets, index):

    if index==len(sets):
        allsubs = []
        allsubs.append({})
    else:

        allsubs = getsubs(sets, index + 1)
        item = list(sets)[index]
        moresubs = []

        for subset in allsubs:
            newsub = set()
            newsub = newsub.union(subset)
            newsub.add(item)
            moresubs.append(newsub)

        allsubs+=moresubs

    # print(allsubs)
    return allsubs


print(getsubs({"a1","a2", "a3"}, 0))
