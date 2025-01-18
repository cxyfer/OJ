#
# @lc app=leetcode id=3165 lang=python3
# @lcpr version=30202
#
# [3165] Maximum Sum of Subsequence With Non-adjacent Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = [0] + nums # 讓 index 從 1 開始
        self.tree = [[0, 0, 0, 0] for _ in range(4 * n)]
        self.build(1, 1, n)

    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o][3] = max(self.nums[left], 0) # f11 
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid)
        self.build(2*o+1, mid + 1, right)
        self.tree[o] = self.merge(2*o, 2*o+1)

    def merge(self, left_child, right_child):
        res = [0, 0, 0, 0] # f00, f01, f10, f11
        l00, l01, l10, l11 = self.tree[left_child]
        r00, r01, r10, r11 = self.tree[right_child]
        res[0] = max(l00 + r10, l01 + r00) # f00 表示不選 left, 不選 right
        res[1] = max(l00 + r11, l01 + r01) # f01 表示不選 left, 可選可不選 right
        res[2] = max(l10 + r10, l11 + r00) # f10 表示可選可不選 left, 不選 right
        res[3] = max(l10 + r11, l11 + r01) # f11 表示可選可不選 left, 可選可不選 right
        return res

    def update(self, o, left, right, idx, val):
        if left == right:
            self.tree[o][3] = max(val, 0)
            return
        mid = (left + right) // 2
        if idx <= mid:
            self.update(2*o, left, mid, idx, val)
        else:
            self.update(2*o+1, mid + 1, right, idx, val)
        self.tree[o] = self.merge(2*o, 2*o+1)

    def query(self):
        return self.tree[1][3]

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = SegmentTree(nums)
        ans = 0
        for pos, x in queries:
            tree.update(1, 0, n - 1, pos, x)
            ans = (ans + tree.query()) % MOD
        return ans
# @lc code=end



#
# @lcpr case=start
# [3,5,9]\n[[1,-2],[0,-3]]\n
# @lcpr case=end

# @lcpr case=start
# [0,-1]\n[[0,-5]]\n
# @lcpr case=end

#

