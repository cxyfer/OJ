"""
CF165E - Compatible Numbers
https://codeforces.com/contest/165/problem/E

SOS DP
"""

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    B = max(A).bit_length()
    U = 1 << B
    f = [-1] * U
    for x in A:
        f[x] = x
    
    for i in range(B):
        for msk in range(U):
            if (msk >> i) & 1:
                f[msk] = max(f[msk], f[msk ^ (1 << i)])
    
    ans = [-1] * n
    for i, x in enumerate(A):
        ans[i] = f[(U - 1) ^ x]
    print(*ans)

if __name__ == '__main__':
    solve()