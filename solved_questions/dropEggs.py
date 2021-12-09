def dropEggs(floors, eggs):
    if floors == 1 or floors == 0 or eggs == 1:
        return floors

    memo = [[0 for _ in range(floors+1)] for _ in range(eggs)]

    for i in range(floors+1):
        memo[0][i] = i

    for j in range(eggs):
        memo[j][0] = 0
    for egg in range(2, eggs+1):
        for floor in range(1, floors + 1):
            minn = 2**31
            for p in range(1, floor+1):
                # print(p, egg, floor)
                temp = max(memo[egg-1 - 1][p -1], memo[egg-1][floor - p])

                if temp < minn:
                    minn = temp


            memo[egg-1][floor] = minn+1
    # print(memo)
    return memo[-1][-1]



print(dropEggs(100, 2))
