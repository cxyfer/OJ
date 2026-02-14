"""
B. 小L的彩球
https://ac.nowcoder.com/acm/contest/120566/B

首先轉化問題：
將所有彩球的位置分別以 L 和 R 表示，則可以寫出一個 LR 字串：L...LR...RL...LR...R
根據題意，LR或RL交替只能發生 t 次，即分組後有恰好 k = t + 1 組，且 L 有 x 個，R 有 n - x 個。
又根據第一組是 L 或 R，可以得到兩種不同的分組方式。
使用隔板法，將 n 個物品分成 k 組，且每組至少有 1 個物品的方案數為 C(n - 1, k - 1)。
"""
MOD = 998244353

MAX_N = int(1e6 + 5)
fact = [1] * (MAX_N + 1)
for i in range(2, MAX_N + 1):
    fact[i] = (fact[i - 1] * i) % MOD
invf = [-1] * (MAX_N + 1)
invf[MAX_N] = pow(fact[MAX_N], MOD - 2, MOD)
for i in range(MAX_N - 1, -1, -1):
    invf[i] = (invf[i + 1] * (i + 1)) % MOD


def comb(n, k):
    return (fact[n] * invf[k] * invf[n - k]) % MOD


def calc(n, k):
    """計算將 n 個物品分成 k 組，且每組至少有 1 個物品的方案數"""
    if k == 0:
        return 1 if n == 0 else 0
    if k > n:
        return 0
    return comb(n - 1, k - 1)


def solve():
    n, x, t = map(int, input().split())

    k = t + 1
    k1, k2 = (k + 1) // 2, k // 2
    ans = (calc(x, k1) * calc(n - x, k2) + calc(x, k2) * calc(n - x, k1)) % MOD
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
