"""
P14359 [CSP-J 2025] 异或和 / xor
https://www.luogu.com.cn/problem/P14359

前綴和 + 枚舉右維護左 + 貪心

定義前綴異或和 s[i] = a[1] ^ a[2] ^ ... ^ a[i]，則區間 [l, r] 的異或和可以表示為 s[r] ^ s[l - 1]
欲使區間 [l, r] 的異或和為 k，需滿足 s[r] ^ s[l - 1] = k，移項得 s[r] ^ k = s[l - 1]
可以用枚舉右維護左，來檢查對於當前右端點是否存在合法的左端點。

此外，由於要劃分成盡量多的互斥區間，需要利用到一點貪心性質。核心是讓未劃分的區間大小盡量大，
因此當我們在枚舉右時若存在合法的左端點，則應該立即劃分，而不應該等待後續的右端點。
"""
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = s = last = 0
    pos = defaultdict(lambda: float('-inf'))
    pos[0] = 0
    for r, x in enumerate(A, start=1):
        s ^= x
        if pos[s ^ k] + 1 > last:  # [pos[s ^ k] + 1, r] 是合法區間
            ans += 1
            last = r
        pos[s] = r
    print(ans)

if __name__ == "__main__":
    solve()