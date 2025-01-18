2#
# @lc app=leetcode.cn id=2610 lang=python3
#
# [2610] 转换二维数组
#
from preImport import *
# @lc code=start
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = defaultdict(list)
        cnt = Counter(nums)
        for k, v in cnt.items():
            for i in range(v):
                ans[i].append(k)
        return list(ans.values())
# @lc code=end

