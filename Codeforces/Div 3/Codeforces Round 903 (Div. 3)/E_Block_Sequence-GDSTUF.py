t = int(input())

def solve(nums):
    # print(nums)
    n = len(nums)
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    ans = n
    for idx, num in enumerate(nums):
        # (n-1)-idx
        # print(idx, num)
        # print((n-1)-idx)
        if num <= (n-1)-idx:
            # print(idx, num)

            ans = min(ans, idx + solve(nums[idx+num+1:]))
            if ans <= idx:
                return ans
    return ans
for case in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    # print("Case #{}: ".format(case+1))
    ans = solve(nums)
    print(ans)