'''
Activity selection is very similar.
'''

def maxMeetings(n, start, end):

    coll = [[start[i], end[i]] for i in range(n)]
    coll.sort(key = lambda x: x[1])

    print(coll)

    last = coll[0][1]
    ans = [1]

    for i in range(1, n):
        if coll[i][0] > last:
            ans.append(i+1)
            last = coll[i][1]

    return ans


print(maxMeetings(6, [1, 3, 0, 5, 8, 5], [2, 4, 5, 7, 9, 9]))

    