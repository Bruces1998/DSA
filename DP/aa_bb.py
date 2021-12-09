def check(start, n, arr):
    if start >= n:
        return True

    if arr[start] == 'a':
        if start + 1 == n:
            return True

        if arr[start+1] == 'a':
            return check(start+2, n, arr)

        if arr[start+1] == 'b':
            if (start + 2) < n and arr[start+2] == 'b':
                return check(start+3, n, arr )

        return False

    if arr[start] == 'b':
        if arr[start+1] == n:
            return False

        if arr[start+1] != 'b':
            return False

        if start + 2 == n:
            return True

        if arr[start+2] == 'a':
            return check(start+3, n, arr)


        return False

    return False



def binding_func(string):
    if string[0] != 'a':
        return False

    return check(0, len(string), string)


if __name__ == "__main__":
    string = input("Enter string:")
    print(binding_func(string))
