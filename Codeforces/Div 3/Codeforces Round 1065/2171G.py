"""
貪心 + Trick

由於 n >= 2，顯然盡可能的使用操作 2 來翻倍是更優的，如果需要使用操作 1，那也是盡量在操作 2 之前使用。
因此可以先計算最大的翻倍次數 k，使得 A[i] * 2^k <= B[i]。
接著在翻倍前，先用操作 1 讓每個數到當前的最大值，也就是使後續翻倍不會超出 B[i] 的範圍的最大值。
令 ci 表示在每次翻倍前，每個數可以執行操作 1 的次數。
則方案數為 sum(ci)! / (c1! * c2! * ... * cn!)

預處理階乘和階乘逆元，即可在 O(1) 時間內計算方案數。
雖然 sum(ci) 可以到達 1e12 級別，但注意到本題給定的模數是 1e6 + 3，
這意味著超過 1e6 + 3 的階乘都會被模數整除，取模後的結果為 0，因此實際上只需要計算到 1e6 + 3 即可。
"""
import math

MAX_N = MOD = int(1e6 + 3)
fact = [0] * MAX_N
fact[0] = 1
for i in range(1, MAX_N):
    fact[i] = fact[i - 1] * i % MOD
invf = [-1] * MAX_N
invf[MAX_N - 1] = pow(fact[MAX_N - 1], MOD - 2, MOD)
for i in range(MAX_N - 2, -1, -1):
    invf[i] = invf[i + 1] * (i + 1) % MOD

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert len(A) == len(B) == n

    # a * 2^k <= b
    # k <= log2(b / a)
    k = min(math.floor(math.log2(b / a)) for a, b in zip(A, B))

    ops = k  # 操作次數，初始化為翻倍次數
    ans = 1  # 方案數
    pow2 = 2 ** k
    for _ in range(k + 1):
        cnt = 0
        for i, (a, b) in enumerate(zip(A, B)):
            v = b // pow2 - a
            ops += v
            cnt += v
            A[i] = b // pow2 * 2
            ans *= invf[v]
            ans %= MOD
        
        pow2 //= 2
        if cnt < MOD:
            ans *= fact[cnt]
            ans %= MOD
        else:
            ans = 0

    print(ops, ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()