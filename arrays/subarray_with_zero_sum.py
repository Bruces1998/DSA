def maxLen(arr, n):

    mapp = {}
    ans = 0
    summ = 0

    for i in range(n):
        summ += arr[i]
        if summ == 0:
            ans = i + 1

        else:
            if mapp.get(summ) is not None:
                ans = max(ans, i - mapp[summ])

            else:
                mapp[summ] = i

    return ans


def subarraySumK(arr, k, n):

    count = 0
    mapp = {}
    summ = 0

    for i in range(n):
        summ += arr[i]

        if summ == k:
            count += 1

        if mapp.get(summ - k) is not None:
            count += mapp[summ -k]

        if mapp.get(summ) is not None:
            mapp[summ] += 1

        else:
            mapp[summ] = 1

    return count