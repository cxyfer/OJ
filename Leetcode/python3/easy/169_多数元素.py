#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from preImport import *
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.solve2(nums)
    """
        1. Hash Table
    """
    def solve1(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            if cnt[num] > len(nums)//2:
                return num
    """
        2. Boyer-Moore Voting Algorithm
    """
    def solve2(self, nums: List[int]) -> int:
        cnt = 0
        candidate = None
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += 1 if num == candidate else -1
        return candidate
# @lc code=end

