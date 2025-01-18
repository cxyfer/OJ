"""
    # 數學
    找中位數，計算所有數字與中位數的差的總和
    tags: CPE49, CPE-240424
"""
T = int(input())

for _ in range(T):
    nums = list(map(int, input().split()))
    n = nums[0]
    s = nums[1:]

    s.sort()
    mid = n // 2
    ans = 0
    for x in s:
        ans += abs(x - s[mid])
    print(ans)