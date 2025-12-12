"""
CSES-1665 Coding Company
https://cses.fi/problemset/task/1665

Open and Close Interval Trick
https://codeforces.com/blog/entry/47764

如果一組的元素 S = {s1, s2, ..., sn}，
則貢獻 max(S) - min(S) 在排序後可以被寫成 (sn - sn-1) + (sn-1 - sn-2) + ... + (s2 - s1)
則當考慮**排序後**的 A[i] 時，A[i] - A[i - 1] 會被貢獻到已經開啟的組中，即已經確定最小值但尚未確定最大值的組中。

定義 f[i][j][tot] 表示處理到第 i 個元素，目前有 j 個未完成的組，累積的 penalty 為 tot 的方法數。
轉移有以下三種情況：
1. 開啟新組 (j -> j + 1)：A[i] 作為某組的最小值，有 1 種選擇。
2. 關閉舊組 (j -> j - 1)：A[i] 作為某組的最大值，可以加入到 j 個組中的任意一個，有 j 種選擇。
3. 加入現有組 (j -> j)：A[i] 既不是最小也不是最大，或者是單獨一組（開啟後立刻關閉），有 j + 1 種選擇。
從 A[i] - A[i - 1] 的距離 d，這段距離會被當前開啟的 j 個組跨越，因此 tot 增加 j * d。
"""
MOD = int(1e9 + 7)

def solve():
    n, V = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    A.sort()
    m = n >> 1  # 開啟的組數最多為 n/2

    f = [[0] * (V + 1) for _ in range(m + 1)]
    f[0][0] = 1
    for i, x in enumerate(A):
        nf = [[0] * (V + 1) for _ in range(m + 1)]
        d = x - (A[i - 1] if i > 0 else 0)
        for j in range(min(i + 1, m) + 1):
            cost = j * d
            for s in range(V - cost + 1):
                v = f[j][s] % MOD
                if not v: continue
                # 1. 開啟新組 (j -> j + 1)
                if j + 1 <= m: nf[j + 1][s + cost] += v
                # 2. 關閉舊組 (j -> j - 1)
                if j > 0: nf[j - 1][s + cost] += v * j
                # 3. 加入現有組或單獨一組 (j -> j)
                nf[j][s + cost] += v * (j + 1)
        f = nf
    print(sum(f[0]) % MOD)

if __name__ == '__main__':
    solve()