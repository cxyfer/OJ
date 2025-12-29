from itertools import groupby

def solve():
    r = list(input().strip())
    n = len(r)
    ans = 0

    if r[0] == 'u':
        r[0] = 's'
        ans += 1
    if r[n - 1] == 'u':
        r[n - 1] = 's'
        ans += 1
    for c, lst in groupby(r):
        if c == 'u':
            ans += len(list(lst)) // 2
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()