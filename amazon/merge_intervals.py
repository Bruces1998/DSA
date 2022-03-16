def merge_intervals(intervals):

    intervals.sort()
    ans = [intervals.pop(0)]

    while intervals:
        current = intervals.pop(0)

        if current[0] > ans[-1][1]:
            ans.append(current)
        else:
            ans[-1][0] = min(ans[-1][0], current[0])
            ans[-1][1] = min(ans[-1][1], current[1])

    return ans