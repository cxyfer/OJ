#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from preImport import *
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        hp = [] # min heap
        for key, val in cnt.items():
            heapq.heappush(hp, (val, key))
            if len(hp) > k:
                heapq.heappop(hp)
        return [key for val, key in hp] # 任意順序都可以
# @lc code=end

