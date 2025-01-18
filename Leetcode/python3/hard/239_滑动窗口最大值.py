#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from preImport import *
# @lc code=start
class Solution:
    """
        Double-ended queue / Monotonic queue
        使用 deque 保存index，並且保證queue中的元素遞增的
        如果新的元素比queue中的某些元素大，那麼這些元素永遠不可能成為最大值，因此將其從queue中刪除
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque() # 從大到小的 Monotonic queue, 保存 index
        ans = []
        for idx, num in enumerate(nums):
            # 1. 插入，從tail移除比nums[i]小的數
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(idx)
            # 2. 若超出窗口範圍則pop
            while q[0] <= idx-k:
                q.popleft()
            # 3. 紀錄答案
            if idx >= k-1: # 前k-1個元素不會有答案
                ans.append(nums[q[0]])
        return ans
# @lc code=end

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)) # [3,3,5,5,6,7]
print(sol.maxSlidingWindow([1],1)) # [1]
# @test([1,3,-1,-3,5,3,6,7],3)=[3,3,5,5,6,7]
# @test([1],1)=[1]