#
# @lc app=leetcode.cn id=3092 lang=python3
#
# [3092] 最高频率的 ID
#
from preImport import *
# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        # return self.solve1(nums, freq)
        return self.solve2(nums, freq)
    """
        1. Hash Table + Lazy Deletion Heap
    """
    def solve1(self, nums: List[int], freq: List[int]) -> List[int]:
        cnt = Counter()
        hp = []
        ans = []
        for x, f in zip(nums, freq):
            cnt[x] += f
            heappush(hp, (-cnt[x], x)) # 用負數是因為 heapq 是最小堆
            while -hp[0][0] != cnt[hp[0][1]]: # 若堆頂的數字的頻率已和當前的頻率不同，則做 Lazy Deletion 
                heappop(hp)
            ans.append(-hp[0][0])
        return ans
    """
        2. Hash Table + Sorted List
    """
    def solve2(self, nums: List[int], freq: List[int]) -> List[int]:
        cnt = Counter()
        sl = SortedList()
        ans = []
        for x, f in zip(nums, freq):
            sl.discard(cnt[x]) # 若有多個相同的頻率，只會刪除一個
            cnt[x] += f
            sl.add(cnt[x])
            ans.append(sl[-1]) 
        return ans
# @lc code=end

