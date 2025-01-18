"""
多骰幾次，有時候會 TLE
"""

import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val = "": sys.stdout.write(str(val) + "\n")

MAXN = 32
is_prime = [True] * (MAXN + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAXN ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN + 1, i):
            is_prime[j] = False

kase = 1
while True:
    try:
        n = int(input().strip())
    except:
        break

    u = (1 << n) - 1
    ans = []
    path = [1] # 一定以 1 開頭
    def dfs(s):
        if s == u:
            if is_prime[path[-1] + path[0]]:
                ans.append(path[:])
            return
        for i in range(n):
            if s & (1 << i):
                continue
            x = i + 1
            if path and not is_prime[path[-1] + x]:
                continue
            path.append(x)
            dfs(s | (1 << i))
            path.pop()
    dfs(1 << 0)

    if kase > 1:
        print()
    print(f"Case {kase}:")
    for p in ans:
        print(" ".join(map(str, p)))
    kase += 1