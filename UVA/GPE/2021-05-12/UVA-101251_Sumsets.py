from collections import defaultdict

while True:
    n = int(input())
    if n == 0:
        break
    nums = [int(input()) for _ in range(n)]
    cnt = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            cnt[nums[i] + nums[j]].append((i, j))
    ans = -float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            for i2, j2 in cnt[nums[j] - nums[i]]:
                if i != i2 and i != j2 and j != i2 and j != j2:
                    ans = max(ans, nums[j])
    print(ans if ans != -float("inf") else "no solution")