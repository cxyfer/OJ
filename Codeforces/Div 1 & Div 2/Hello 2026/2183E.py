from collections import defaultdict

MOD = 998244353

MAX_M = 3005
divs = [[] for _ in range(MAX_M)]
for i in range(1, MAX_M):
    for j in range(i, MAX_M, i):
        divs[j].append(i)

def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    if A[0] not in [0, 1]:
        print(0)
        return

    # f[i][v] 表示第 i 個數值為 v 的方案數，滾動掉 i 的維度
    f = defaultdict(int)
    f[1] = 1
    for i in range(1, n):
        nf = defaultdict(int)
        for v in f.keys():
            for d in divs[v]:
                if (nv := v + d) > m:
                    break
                if A[i] == 0 or nv == A[i]:
                    nf[nv] = (nf[nv] + f[v]) % MOD
        f = nf

    print(sum(f.values()) % MOD)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()