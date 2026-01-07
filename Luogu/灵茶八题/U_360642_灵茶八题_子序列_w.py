"""
U360642 灵茶八题 - 子序列 ^w+
https://www.luogu.com.cn/problem/U360642

按位拆分 + 貢獻法
- 如果某一位上沒有 1，那麼該位對答案的貢獻是 0。
- 如果有 c 個 1，那麼根據二項式定理，從 c 個 1 選偶數個的方案數為 2^(c-1)，選奇數個的方案數也是 2^(c-1)。
  剩餘 n - c 個數任意選擇都不會影響奇偶性，因此有 2^(n-c) 種方案。
  根據乘法原理，第 b 位有貢獻的方案數為 2^(c-1) * 2^(n-c) = 2^(n-1) 種
所以第 b 位對答案的貢獻是 2^(n-1) * 2^(b) = 2^(n-1+b)。
"""
MOD = int(1e9 + 7)

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = 0
    for b in range(32):
        c = 0
        for x in A:
            c += (x >> b) & 1
        if c > 0:
            ans += pow(2, b + n - 1, MOD)
            ans %= MOD
    print(ans)

if __name__ == "__main__":
    solve()