"""
    依照S給出的順序，倒著做
"""
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    s = input()

    b = list()
    l, r = 0, n - 1
    for i in range(n):
        if s[i] == 'L':
            b.append(arr[l])
            l += 1
        else:
            b.append(arr[r])
            r -= 1
    total = 1
    ans = [1] * n
    for i in range(n-1, -1, -1):
        total *= b[i]
        total %= m
        ans[i] = total
    print(*ans)