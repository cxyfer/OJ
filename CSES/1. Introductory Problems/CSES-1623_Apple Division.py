"""
    Enumeration + Bitmask
"""
n = int(input())
nums = list(map(int, input().split()))
s = sum(nums)
ans = s
for i in range(1 << n):
    s1 = 0
    for j in range(n):
        if i & (1 << j):
            s1 += nums[j]
    s2 = s - s1
    ans = min(ans, abs(s1 - s2))
print(ans)