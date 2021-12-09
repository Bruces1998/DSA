def no_three_consecutive(summ, arr):
    n = len(arr)
    if n == 0:
        return summ

    if n == 1:
        return arr[0]+summ

    if n == 2:
        return arr[0]+arr[1]+summ

    case1 = no_three_consecutive(summ, arr[1:])
    case2 = no_three_consecutive(summ+arr[0]+arr[1], arr[3:])
    case3 = no_three_consecutive(summ+arr[0], arr[2:])

    return max(case1, max(case2, case3))


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(no_three_consecutive(0, arr))
