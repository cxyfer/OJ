"""
SPOJ - KOSARE
https://www.spoj.com/problems/KOSARE/en/
SOS DP + PIE
"""
from functools import reduce
MOD = int(1e9 + 7)

def solve():
    n, B = map(int, input().split())
    U = 1 << B
    f = [0] * U
    for _ in range(n):
        _, *bits = map(int, input().split())
        x = reduce(lambda x, y: x | (1 << (y - 1)), bits, 0)
        f[x] += 1

    for i in range(B):
        s = 0
        while s < U:
            s |= (1 << i)
            f[s] += f[s ^ (1 << i)]
            s += 1
    
    ans = 0
    for s in range(U):
        term = pow(2, f[s], MOD) - 1
        if (B - s.bit_count()) & 1:
            term = -term
        ans = (ans + term) % MOD
    print(ans)

if __name__ == '__main__':
    solve()