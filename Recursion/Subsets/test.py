
nums = [2,-1,0,4,-2,-9]

def hello(nums):
    target = sum(nums) // 2
    n = len(nums)
    print(target)
    print(n+1)

    dp = [[False for i in range(target+1)] for j in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    print(dp)

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    candidates = []

    for i in range(1, target + 1):
        if dp[n][i]:
            candidates.append(i)

    print(candidates)

    min_diff = sum(nums)

    for candidate in candidates:
        diff = abs(sum(nums) - 2 * candidate)
        min_diff = min(min_diff, diff)

    return min_diff


print(hello(nums))