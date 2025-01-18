from math import gcd

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            ans = max(ans, gcd(nums[i], nums[j]))
    print(ans)