#
# @lc app=leetcode id=703 lang=python3
# @lcpr version=30204
#
# [703] Kth Largest Element in a Stream
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hp = []  # 維護一個大小為 k 的 min heap
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        heappush(self.hp, val)
        if len(self.hp) > self.k:
            heappop(self.hp)
        return self.hp[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end



