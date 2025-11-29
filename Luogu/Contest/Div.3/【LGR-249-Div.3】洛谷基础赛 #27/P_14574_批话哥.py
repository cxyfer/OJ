"""
P14574 批话哥
https://www.luogu.com.cn/problem/P14574

根據題目要求，計算每個學生在每個科目上的得分，最後再加總即可。
時間複雜度為 O(nm + k)，空間複雜度為 O(nm)。
由於相同科目的成績不會重複出現多次，因此也可以直接加到每個學生的總分中。
時間複雜度為 O(n + k)，空間複雜度為 O(n)。
"""
def solve():
    n, m, k, l, r = map(int, input().split())
    ans = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y, v = map(int, input().split())
        x, y = x - 1, y - 1
        if v <= l:
            ans[x][y] = 100
        elif v >= r:
            ans[x][y] = 0
        else:
            ans[x][y] = v
    print(*map(sum, ans))

if __name__ == "__main__":
    solve()