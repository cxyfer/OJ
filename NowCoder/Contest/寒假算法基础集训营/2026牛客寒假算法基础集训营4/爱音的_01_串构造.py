"""
F. 爱音的01串构造
https://ac.nowcoder.com/acm/contest/120564/F

子字串的總數為 tot = n(n+1)/2，令只包含 0 的子字串數量為 cnt0，只包含 1 的子字串數量為 cnt1，
則包含 01 的子字串數量為 tot - cnt0 - cnt1。

cost = 0 * cnt1 + 1 * cnt0 + 2 * (tot - cnt0 - cnt1)
     = 2 * tot - cnt0 - 2 * cnt1
最大化 cost 等價於最小化 cnt0 + 2 * cnt1。

可以得到最優的構造為 010...10 或 101...01，即 01 交替出現。
然而這只能發生在 abs(a - b) <= 1 時。

由於一個長度為 ln 的連續 0，可以對 cnt0 貢獻 l * (l + 1) / 2 次，連續的 1 同理。
因此需要將多餘的數字分散到連續的相同的數字中。
"""
def solve():
    a, b = map(int, input().split())

    ans = []
    def build(a: int, b: int, x: str, y: str) -> None:
        q, r = divmod(a, b + 1)
        for _ in range(b):
            ans.extend([x] * (q + (r > 0)))
            ans.append(y)
            r -= 1
        ans.extend([x] * q)
        assert len(ans) == a + b
    
    if a >= b:
        build(a, b, '0', '1')
    else:
        build(b, a, '1', '0')

    print(*ans, sep='')

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()