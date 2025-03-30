#
# @lc app=leetcode id=1570 lang=python3
#
# [1570] Dot Product of Two Sparse Vectors
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class SparseVector1:
    def __init__(self, nums: List[int]):
        self.mp = defaultdict(int)
        for i, x in enumerate(nums):
            if x != 0:
                self.mp[i] = x

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k, v in self.mp.items():
            res += v * vec.mp[k]
        return res
    
class SparseVector2:
    def __init__(self, nums: List[int]):
        self.pairs = [(i, x) for i, x in enumerate(nums) if x != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        i = j = 0
        while i < len(self.pairs) and j < len(vec.pairs):
            if self.pairs[i][0] == vec.pairs[j][0]:
                res += self.pairs[i][1] * vec.pairs[j][1]
                i += 1
                j += 1
            elif self.pairs[i][0] < vec.pairs[j][0]:
                i += 1
            else:
                j += 1
        return res

# SparseVector = SparseVector1
SparseVector = SparseVector2
# @lc code=end
v1 = SparseVector([1, 0, 0, 2, 3])
v2 = SparseVector([0, 3, 0, 4, 0])
print(v1.dotProduct(v2))
