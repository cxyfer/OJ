"""
F - 薪得体会
https://ac.nowcoder.com/acm/contest/95338/F

貪心 + 排序

能拿到最高的薪資一定是某份 offer 的 a + b，或是最大的 a。
後者發生在所有 offer 的 a + b 都 <= 最大的 a 的情況。

考慮前者，如果要拿到某份 offer 的 ai + bi，則需要滿足以下條件之一：
- 有其他 offer 的 aj >= ai
- 或有其他 offer 的 aj + bj >= ai，且又有 ak >= aj

可以由 a + b 遞增的順序，來判斷是否可以拿到某份 offer 的 a + b。
不過這裡我不知道該怎麼說明以及證明正確性。

令 ans 表示可以拿到最高的薪資，初始值為 0，則有以下幾種情況：
- 若 ans >= ai，則可以拿到這份 offer 的薪資 ai + bi
- 若 ans < ai，則可以先接受這份 offer 的 ai，然後再拿到其他 offer 的薪資 aj + bj
- 此外，也能直接接受這份 offer 的 ai
"""
def solve():
    n = int(input())
    offers = [tuple(map(int, input().split())) for _ in range(n)]
    assert len(offers) == n

    offers.sort(key = lambda p: p[0] + p[1])
    ans = 0
    for i, (a, b) in enumerate(offers):
        if ans >= a:  # 有其他 offer 的薪資比這份的 a 還高，這份可以拿到 a + b
            ans = max(ans, a + b)
        else:  # 可以先接受這份 offer，然後再拿到其他 offer 的 a + b
            ans = max(ans, offers[i - 1][0] + offers[i - 1][1] if i > 0 else 0)
        ans = max(ans, a)  # 考慮 a 大於其他所有 offer 的 a + b 的情況
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()