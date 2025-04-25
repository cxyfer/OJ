"""
【虾皮】20250423_1_田忌赛马（Horse Racing）
https://niumacode.com/problem/P1593
"""

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

l1, r1 = 0, n - 1
l2, r2 = 0, n - 1
ans = 0
while l1 <= r1:
    if arr1[r1] > arr2[r2]:
        ans += 200
        r1 -= 1
        r2 -= 1
    elif arr1[l1] > arr2[l2]:
        ans += 200
        l1 += 1
        l2 += 1
    else:
        if arr1[l1] < arr2[r2]:
            ans -= 200
        l1 += 1
        r2 -= 1
print(ans)