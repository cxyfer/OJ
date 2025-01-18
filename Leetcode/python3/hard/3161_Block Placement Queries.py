#
# @lc app=leetcode id=3161 lang=python3
# @lcpr version=30203
#
# [3161] Block Placement Queries
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    維護三個性質
    - ld: left distance, 從左邊到最近的障礙物的距離，無障礙物為 -1
    - rd: right distance, 從右邊到最近的障礙物的距離，無障礙物為 -1
    - mx: 最大可放置的連續物體長度，單點為 0
        - 若無障礙物， [1, 2] 區間可放置的最大長度為 1
"""
class SegmentTree:
    def __init__(self, n: int):
        self.tree = [[0, 0, 0] for _ in range(4 * n)]  # (ld, rd, mx)
        self.build(1, 0, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = [-1, -1, 0] # (ld, rd, mx)
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)
        
    """
        合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    """
    def merge(self, left_part, right_part, left, mid, right):
        lld, lrd, lmx = left_part
        rld, rrd, rmx = right_part
        res = [lld, rrd, 0]

        t = 1 # 中間的部分最大可放置的連續物體長度
        t += (mid - left) if lrd == -1 else lrd # 從中間往左延伸
        t += (right - (mid+1)) if rld == -1 else rld # 從中間往右延伸
        res[2] = max(lmx, rmx, t) # [left, right] 區間最大可放置的連續物體長度

        if lld == -1:
            res[0] = -1 if rld == -1 else (mid - left + 1 + rld) # 往右延伸
        if rrd == -1:
            res[1] = -1 if lrd == -1 else (right - (mid+1) + 1 + lrd) # 往左延伸
        return res

    def update(self, o, left, right, idx): # 將 idx 位置標記為已放置障礙物
        if left == right: # leaf
            self.tree[o] = [0, 0, 0] # (ld, rd, mx)
            return
        mid = (left + right) // 2
        if idx <= mid:
            self.update(2*o, left, mid, idx)
        else:
            self.update(2*o+1, mid + 1, right, idx)
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)
 
    def query(self, o, left, right, l, r):
        if left == l and r == right:
            return self.tree[o]
        mid = (left + right) // 2
        if r <= mid: # 只需要查詢左半部分
            return self.query(2*o, left, mid, l, r)
        if mid < l: # 只需要查詢右半部分
            return self.query(2*o+1, mid + 1, right, l, r)
        left_part = self.query(2*o, left, mid, l, mid) # 左半部分
        right_part = self.query(2*o+1, mid + 1, right, mid + 1, r) # 右半部分
        return self.merge(left_part, right_part, l, mid, r) # 合併左右兩部分

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = min(int(5e4), 3 * len(queries))
        seg = SegmentTree(n)
        ans = []
        for op, *args in queries:
            if op == 1:
                x, = args
                seg.update(1, 0, n, x)
            else:
                x, sz = args
                ans.append(True if seg.query(1, 0, n, 0, x)[2] >= sz else False)
        return ans
# @lc code=end

sol = Solution()
print(sol.getResults([[1,2],[2,3,3],[2,3,1],[2,2,2]])) # [False, True, True]
print(sol.getResults([[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]])) # [True, True, False]
print(sol.getResults([[2,1,1]])) # [True]
print(sol.getResults([[2,1,2]])) # [False]
print(sol.getResults([[1,4],[2,1,2]])) # [False]
print(sol.getResults([[1,1],[2,4,3]])) # [True]

#
# @lcpr case=start
# [[1,2],[2,3,3],[2,3,1],[2,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]\n
# @lcpr case=end

#

