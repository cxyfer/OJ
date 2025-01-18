import sys
from functools import cache
sys.setrecursionlimit(int(1e5))

def query(l, r):
    print(f"? {l} {r}", flush=True)
    return int(input())

def answer(ans):
    print(f"! {ans}", flush=True)

t = int(input())
for _ in range(t):
    n = int(input())

    A = [0] * (n + 2)
    f = [0] * (n + 2)
    for i in range(1, n):
        f[i] = query(i, n)
            
    D = [0] * (n + 2) # D[i] 表示以 i 為開頭的子序列數量 
    for i in range(1, n):
        D[i] = f[i] - f[i + 1]

    s = [''] * (n + 1)
    @cache
    def dfs(i, cnt):
        if i == 0:
            return (1, ''.join(s[1:n+1]))
        if D[i] < 0:
            return (0, '')

        if D[i] > 0:
            s[i] = '0'
            if D[i] != cnt:
                return (0, '')
            possible, res = dfs(i - 1, cnt)
            if possible != 1:
                res = ''
        else:
            if cnt > 0:
                s[i] = '1'
                possible, res = dfs(i - 1, cnt + 1)
                if possible != 1:
                    res = ''
            else:
                s[i] = '0'
                p0, res0 = dfs(i - 1, cnt)
                s[i] = '1'
                p1, res1 = dfs(i - 1, cnt + 1)
                possible = p0 + p1
                if p0 == 1 and p1 != 1:
                    res = res0
                elif p1 == 1 and p0 != 1:
                    res = res1
                else:
                    res = ''
        possible = 2 if possible >= 2 else possible
        return possible, res

    possible, ans = dfs(n, 0)
    ans = ans if possible == 1 else 'IMPOSSIBLE'
    answer(ans)
    dfs.cache_clear()