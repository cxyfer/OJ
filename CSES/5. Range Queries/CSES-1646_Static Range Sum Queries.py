n, q = map(int, input().split())
nums = list(map(int, input().split()))
pre = [0] * (n + 1)
for i, x in enumerate(nums):
    pre[i + 1] = pre[i] + x
for _ in range(q):
    a, b = map(int, input().split())
    print(pre[b] - pre[a - 1])