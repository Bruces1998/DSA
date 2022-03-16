def maxProduct(nums):
    max_prod = minProd = ans = nums[0]

    for i in range(1, len(nums)):
        x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
        y = min(nums[i], max_prod*nums[i], min_prod*nums[i])

        max_prod, min_prod = x, y
        ans = max(ans, max_prod)

    return ans