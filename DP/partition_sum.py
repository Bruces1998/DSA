#recursion

def partSumUtil(index, target):
    if target == 0:
        return True
    
    if index == 0:
        return arr[index] == target

    notTaken = partSumUtil(index - 1, target)

    if arr[index]> target:
        return notTaken

    taken = partSumUtil(index - 1, target - arr[index])
    

    return taken or notTaken


#DP

def ptUtil(nums):
    arr_sum = 0

    for i in nums:
        arr_sum += i

    if arr_sum % 2 != 0:
        return False
    
    arr_sum /= 2

    mapp = [[False]*arr_sum+1]* len(nums)

    for i in range(len(nums)):
        mapp[i][0] = True

    for j in range(arr_sum + 1):
        if j == nums[0]:
            nums[0][i] = True


    for i in range(1, len(nums)):
        for j in range(arr_sum+1):

            if nums[i] > j:
                mapp[i][j] = mapp[i - 1][j]
            else:
                mapp[i][j] = mapp[i - 1][j] or mapp[i - j][j - nums[i]]

    
    return mapp[len(nums) - 1][arr_sum]