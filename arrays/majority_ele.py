def majority_ele(arr):
    count = 0
    candidate = 0

    for ele in arr:
        if count == 0:
            candidate = ele

        if candidate == ele:
            count += 1

        else:
            count -= 1

    return candidate


def majority_ele_2(arr):
    c1 = 0
    c2 = 0
    ele_1 = -1
    ele_2 = -1

    for ele in arr:
        if ele == ele_1:
            c1 += 1
        
        elif ele == ele_2:
            c2 += 1

        elif c1 == 0:
            ele_1 = ele
            c1 = 1

        elif c2 == 0:
            ele_2 = ele
            c2 = 1

        else:
            c1 -= 1
            c2 -= 1

    ans = []

    c1 = c2 = 0
    for ele in arr:
        if ele == ele_1:
            c1 += 1

        elif ele == ele_2:
            c2 += 1

    if c1 > len(arr)//3:
        ans.append(ele_1)
    
    if c2 > len(arr)//3:
        ans.append(ele_2)

    return ans