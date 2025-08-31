"""
CF383E - Vowels
https://codeforces.com/contest/383/problem/E
SOS DP

正難則反，令 S 為子音集合、且 f[S] 為所有字母都是子音的單字數量，
則所求為 (n - f[S]) 。
"""

def solve():
    n = int(input())
    B = 24
    U = 1 << B

    f = [0] * U
    for _ in range(n):
        word = input().strip()
        s = 0
        for ch in word:
            s |= 1 << (ord(ch) - ord('a'))
        f[s] += 1
    
    for i in range(B):
        # for s in range(U):
        #     if (s >> i) & 1:
        #         f[s] += f[s ^ (1 << i)]
        s = 0
        while s < U:
            s |= (1 << i)
            f[s] += f[s ^ (1 << i)]
            s += 1
    
    ans = 0
    for s in range(1 << B):
        ans ^= (n - f[s ^ (U - 1)]) ** 2
    print(ans)

if __name__ == '__main__':
    solve()