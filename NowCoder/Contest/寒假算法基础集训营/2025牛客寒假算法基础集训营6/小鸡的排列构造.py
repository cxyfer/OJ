"""
H - 小鸡的排列构造
https://ac.nowcoder.com/acm/contest/95338/H

根據題意，可以考慮限制區間大小為奇數和偶數兩種情況。
對於所有合法的限制區間，區間內的大小關係都需要為錯排。

偶數的情況只需要構造 [n, n - 1, ..., 1] 即可滿足所有限制。
奇數的情況可以由長度為 3 的兩種錯排 (2, 3, 1) 和 (3, 1, 2) 組合而成。
雖然看完題解還是不知道為甚麼，但將 [n, n - 1, ..., 1] 每兩個元素交換即可滿足。
"""
def solve():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(q)]

    ans = list(range(n, 0, -1))
    if (queries[0][1] - queries[0][0] + 1) & 1:
        for i in range(0, n - 1, 2):
            ans[i], ans[i + 1] = ans[i + 1], ans[i]
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()