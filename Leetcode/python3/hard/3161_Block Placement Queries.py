#
# @lc app=leetcode id=3161 lang=python3
# @lcpr version=30203
#
# [3161] Block Placement Queries
#


# @lcpr-template-start
from preImport import *

# @lcpr-template-end
"""
本題的狀態設計其實和 53. Maximum Subarray 蠻類似的，可以

對於每個區間 [left, right]，維護四個性質：
- sz: 區間長度
- dl: 從 left 往右到最近的障礙物的距離，無障礙物為 sz
- dr: 從 right 往左到最近的障礙物的距離，無障礙物為 sz
- mx: 最大可放置的連續物體長度，單點為 0，若無障礙物為 sz - 1

合併兩個區間 [left, mid] 和 [mid + 1, right] 時，中間會產生一個新的間隔 mid_gap：
- mid_gap 可以由 ls.dr 和 rs.dl 共同決定，加上原本兩側的最大間隔，因此 mx = max(ls.mx, rs.mx, mid_gap)
- dl 和 dr 的更新則需要考慮是否有障礙物，以及是否能從一側延伸到另一側。

跑很慢是因為為了方便展示邏輯，我把合併寫在 SegNode.__add__ 裡面了，想必各位大神有的是方法優化。
"""
# @lc code=start
class SegNode:
    def __init__(self, dl=1, dr=1, mx=0, sz=1) -> None:
        # 從左端點/右端點到最近的障礙物的距離，無障礙物時設為 sz
        self.dl, self.dr = dl, dr
        # [left, right] 區間最大可放置的連續物體長度
        self.mx = mx
        self.sz = sz

    def __add__(ls, rs):
        dl, dr = ls.dl, rs.dr
        sz = ls.sz + rs.sz

        mid_gap = 1  # 考慮中間的間隙
        mid_gap += ls.sz - 1 if ls.dr == ls.sz else ls.dr  # 從中間往左延伸
        mid_gap += rs.sz - 1 if rs.dl == rs.sz else rs.dl  # 從中間往右延伸
        mx = max(mid_gap, ls.mx, rs.mx)

        if ls.dl == ls.sz:  # 左區間無障礙物
            dl = sz if rs.dl == rs.sz else (ls.sz + rs.dl)  # 往右延伸
        if rs.dr == rs.sz:  # 右區間無障礙物
            dr = sz if ls.dr == ls.sz else (rs.sz + ls.dr)  # 往左延伸

        return SegNode(dl, dr, mx, sz)


class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        # 注意我們實際上是維護 [0, n] 的 n + 1 個位置
        sz = 1 << ((n + 1).bit_length() + 1)
        self.tree = [None for _ in range(sz)]
        self.buidl(1, 0, self.n)

    def buidl(self, o: int, left: int, right: int):
        if left == right:  # leaf
            self.tree[o] = SegNode()
            return
        mid = (left + right) // 2
        self.buidl(2 * o, left, mid)
        self.buidl(2 * o + 1, mid + 1, right)
        self.pushup(o)

    def pushup(self, o: int) -> None:
        self.tree[o] = self.tree[2 * o] + self.tree[2 * o + 1]

    def update(self, o: int, left, right, idx):  # 將 idx 位置標記為已放置障礙物
        if left == right:  # leaf
            node = self.tree[o]
            node.dl = node.dr = node.mx = 0
            return
        mid = (left + right) // 2
        if idx <= mid:
            self.update(2 * o, left, mid, idx)
        else:
            self.update(2 * o + 1, mid + 1, right, idx)
        self.pushup(o)

    def query(self, o, left, right, l, r):
        if left == l and r == right:
            return self.tree[o]
        mid = (left + right) // 2
        if r <= mid:  # 只需查詢左子樹
            return self.query(2 * o, left, mid, l, r)
        if mid < l:  # 只需查詢右子樹
            return self.query(2 * o + 1, mid + 1, right, l, r)
        ls = self.query(2 * o, left, mid, l, mid)  # 左半部分
        rs = self.query(2 * o + 1, mid + 1, right, mid + 1, r)  # 右半部分
        return ls + rs


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = max(q[1] for q in queries)
        seg = SegmentTree(n)
        ans = []
        for op, *args in queries:
            if op == 1:
                (x,) = args
                seg.update(1, 0, n, x)
            else:
                x, sz = args
                ans.append(True if seg.query(1, 0, n, 0, x).mx >= sz else False)
        return ans
# @lc code=end

sol = Solution()
print(sol.getResults([[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]))  # [False, True, True]
print(
    sol.getResults([[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]])
)  # [True, True, False]
print(sol.getResults([[2, 1, 1]]))  # [True]
print(sol.getResults([[2, 1, 2]]))  # [False]
print(sol.getResults([[1, 4], [2, 1, 2]]))  # [False]
print(sol.getResults([[1, 1], [2, 4, 3]]))  # [True]
print(sol.getResults([[2,2,3]]))  # [False]


#
# @lcpr case=start
# [[1,2],[2,3,3],[2,3,1],[2,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]\n
# @lcpr case=end

#
