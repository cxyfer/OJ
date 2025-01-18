from collections import defaultdict

T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    s = [0] * n
    for i in range(1, n):
        s[i] = s[i - 1] + (A[i] if A[i] == A[i - 1] else 0)
    # f[i] 表示前 i+1 個元素中所能獲得的最大得分
    f = [0] * (n)
    lst = defaultdict(int)
    for i, x in enumerate(A):
        f[i] = f[i - 1] # 不選
        if x in lst:
            f[i] = max(f[i], f[lst[x] + 1] + x + s[i] - s[lst[x] + 1]) # 選
        lst[x] = i
    print(f[-1])