"""
abc408_d - Flip to Gather
https://atcoder.jp/contests/abc408/tasks/abc408_d
枚舉右維護左

假設保留的區間是 (l, r]，那麼需要的操作次數為：區間內0的個數 + 區間外1的個數。

用前綴和來表示：
- 區間內0的個數：s_{0, r} - s_{0, l} 
- 區間外1的個數：tot_1 - (s_{1, r} - s_{1, l})
而 s_{0, r} - s_{0, l} 可以改成用 1 的前綴和來表示：(r - l) - (s_{1, r} - s_{1, l})

整理一下，將 l 和 r 的部分分開：
  tot_1 + (r - l) - 2 * (s_{1, r} - s_{1, l})
= tot_1 + (r - 2 * s_{1, r}) - (l - 2 * s_{1, l})
"""
def solve():
    n = int(input())
    S = input()
    assert len(S) == n
    tot_1 = S.count('1')
    ans = s = mx = 0
    for r, ch in enumerate(S, 1):
        s += (ch == '1')
        ans = min(ans, (r - 2 * s) - mx)
        mx = max(mx, r - 2 * s)  # 維護最大的 l - 2 * s_{1, l}
    print(ans + tot_1)

t = int(input())
for _ in range(t):
    solve()