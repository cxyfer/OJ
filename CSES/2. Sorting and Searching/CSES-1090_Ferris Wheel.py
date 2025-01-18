""" CSES-1090 Ferris Wheel
    Two pointers + Sort
"""
n, x = map(int, input().split())
nums = sorted(map(int, input().split()))
ans = 0

l, r = 0, n - 1
while l <= r:
    if nums[l] + nums[r] <= x:
        l += 1
    r -= 1
    ans += 1
print(ans)