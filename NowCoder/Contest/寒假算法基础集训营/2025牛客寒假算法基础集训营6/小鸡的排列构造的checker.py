"""
I - 小鸡的排列构造的checker
https://ac.nowcoder.com/acm/contest/95338/I

樹狀陣列 + 離線查詢

query(l, r, c) 等同於求 l 加上 nums[l:r+1] 中 < nums[c] 的元素個數
我們可以令 < nums[c] 的位置為 1，其餘位置為 0，如此便能使用 BIT 來求解 (l, r) 區間內 1 的個數。

由於 c 是可變的，我們不太可能對所有 c 都建一顆 BIT，考慮離線查詢。
我們可以將所有詢問按照 nums[c] 分組，然後由小到大逐步加入 nums[c] 的貢獻，最後再求解。
"""

class BIT:
    __slots__ = ['tree']

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= (k & -k)
        return res

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)

def solve():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    mp = {x: i for i, x in enumerate(A, 1)}

    ans = [-1] * q
    queries = [[] for _ in range(n + 1)]
    for qid in range(q):
        l, r, k = map(int, input().split())
        queries[A[k-1]].append((l, r, qid))

    bit = BIT(n)
    for x in range(1, n + 1):
        for l, r, qid in queries[x]:
            ans[qid] = l + bit.query(l, r)
        bit.add(mp[x], 1)
    print(*ans, sep='\n')

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()