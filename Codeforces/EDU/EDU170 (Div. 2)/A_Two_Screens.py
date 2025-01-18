T = int(input())

for _ in range(T):
    s = input()
    t = input()

    n, m = len(s), len(t)
    i = 0
    while i < n and i < m and s[i] == t[i]:
        i += 1
        
    ans = n + m - (i - 1 if i >= 2 else 0)
    print(ans)