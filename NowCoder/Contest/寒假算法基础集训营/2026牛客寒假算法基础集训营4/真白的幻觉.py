"""
G. 真白的幻觉
https://ac.nowcoder.com/acm/contest/120564/G

回溯打表
由於交換 x 中的位數不影響 f(x) 的值，因此不妨讓 x 的數位遞增。
又數位 1 對 f(x) 沒有貢獻，因此從 2 考慮即可。
"""

from collections import defaultdict

def f(n: int) -> int:
    p = 1
    while n:
        n, d = divmod(n, 10)
        p *= d
    return p

def g(n: int) -> int:
    if n < 10:
        return 0
    return 1 + g(f(n))

def solve():
    max_g = 0
    ans = defaultdict(int)
    def dfs(x: int, pre: int) -> None:
        if x > int(1e18):
            return
        nonlocal max_g
        gx = g(x)
        if gx > max_g:
            max_g = gx
            ans.clear()
            ans[f(x)] = x
        elif gx == max_g:
            ans[f(x)] = max(ans[f(x)], x)
            
        for d in range(pre, 10):
            dfs(x * 10 + d, d)

    dfs(0, 2)
    a, b = list(ans.values())[:2]
    # a, b = 344444444666777777, 336666777779999999
    print(a, b)

    assert a <= int(1e18) and b <= int(1e18)
    assert f(a) != f(b)
    assert g(a) == g(b)

if __name__ == "__main__":
    solve()