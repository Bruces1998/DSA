def longestConsecutive(arr):
    mapp = {}
    for ele in arr:
        mapp[ele]

    longest_steak = 0

    for i in range(len(arr)):
        if mapp.get(arr[i]-1) is None:
            current = arr[i]
            steak = 1

            while(mapp.get(current+1)):
                current += 1
                steak += 1

            longest_steak = max(longest_steak, steak)


    return longest_steak
