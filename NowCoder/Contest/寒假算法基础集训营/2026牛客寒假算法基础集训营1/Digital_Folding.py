"""
G. Digital Folding
https://ac.nowcoder.com/acm/contest/120561/G

注意到除了當 r = 10^d 時， fold(x) 的最大值的位數和 r 的位數相同，
由於翻轉後以 9 開頭更優，故可以枚舉是否可以將 r 的最後 k 位變成 9。
"""
def solve():
    l, r = map(int, input().split())

    def fold(x):
        return int(str(x)[::-1])

    ans = fold(r)
    base = 1
    while r > 0:
        r, d = divmod(r, 10)
        if d > 0:
            v = r * base * 10 + d * base - 1
            if l <= v:
                ans = max(ans, fold(v))
        base *= 10
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()