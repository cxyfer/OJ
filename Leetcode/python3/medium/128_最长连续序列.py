21#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from preImport import *
# @lc code=start
class Solution:
    """
        Hash Table
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        st = set(nums) # 這邊用 set 會比用 list 快很多
        for num in nums:
            if num - 1 not in st: # 確定 num 是一個連續序列的開頭   
                cur = num
                cur_len = 1
                while cur+1 in st:
                    cur += 1
                    cur_len += 1
                ans = max(ans, cur_len) # 更新答案
        return ans
# @lc code=end

