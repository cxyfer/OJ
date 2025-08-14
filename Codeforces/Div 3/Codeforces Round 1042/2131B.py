t = int(input())

def solve():
    n = int(input())
    ans = [-1] * n
    for i in range(1, n - 1, 2):
        ans[i] = 3
    if (n & 1) ^ 1:
        ans[n - 1] = 2
    print(*ans)

for _ in range(t):
    solve()