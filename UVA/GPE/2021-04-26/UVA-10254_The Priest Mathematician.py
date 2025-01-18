""""
f[n] = min_{1<=k<=n} (f[k]*2 + g[n-k])
g[n] = 2^n - 1

從結果可以找到規律，將 f[i] 分成多組，第 m 組有 m 個數
f[i] = f[i-1] + 2^(m-1)，其中 m 是第 i 個數所在的組
"""

import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

N = int(1e4 + 5)

f = [0] * N
i = m = p = 1
while i <= 10000:
    for _ in range(m):
        # f[i] = f[i - 1] + pow(2, m - 1)
        f[i] = f[i - 1] + p
        i += 1
        if i > 10000:
            break
    m += 1
    p <<= 1

while True:
    try:
        n = int(input())
    except:
        break
    print(f[n])