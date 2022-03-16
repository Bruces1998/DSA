def validParentheses(s):
    stack = []
    _open = {"(":1, "[":1, "{":1}
    _close = {")":1, "]":1, "}":1}

    for i in s:
        if _open.get(i) is not None:
            stack.append(i)

        else:
            if stack == []:
                return False
            
            item = stack.pop(-1)
            for a, b in zip(_open, _close):
                if i==b and item != a:
                    return False

    return not stack
print(validParentheses(input("Enter string: ")))
