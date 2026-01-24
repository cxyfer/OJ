from collections import defaultdict

def solve():
    n = int(input())
    P = list(map(float, input().split()))

    # f[i][j] 表示考慮前 i 個硬幣，得到 j 個正面的機率
    f = defaultdict(float)
    f[0] = 1
    for p in P:
        nf = defaultdict(float)
        for j, q in f.items():
            nf[j + 1] += q * p
            nf[j] += q * (1 - p)
        f = nf
    print(sum(q for j, q in f.items() if j > n - j))

if __name__ == "__main__":
    solve()