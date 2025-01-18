#
# @lc app=leetcode.cn id=1424 lang=python3
#
# [1424] 对角线遍历 II
#
from preImport import *
# @lc code=start
class Solution:
    """
        對於 matrix[i][j]，其對角線編號為 i+j
    """
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        lst = defaultdict(list)
        for i, row in enumerate(nums):
            for j, v in enumerate(row):
                lst[i+j].append(v)
        ans = []
        for k in sorted(lst.keys()):
            ans += lst[k][::-1] # 逆序
        return ans
# @lc code=end

