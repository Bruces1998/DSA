def get_min(N, K, T, t):
    
    scream_count = [0]*N
    if t[0] <= T:
        scream_count[0] = 1

    for i  in range(1, N):

        if t[i] <= T:
            scream_count[i] = 1

        else:
            if scream_count[i-1] == 1:
                if K != 0:
                    K -= 1

                else:
                    scream_count[i] = 1


    return sum(scream_count)


print(get_min(5, 1, 42, [13, 37, 47, 11, 42]))


