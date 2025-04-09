#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Max Heap + Lazy Deletion : O(nlogn)
使用 Max Heap 維護窗口內的元素，並且使用 Lazy Deletion 來刪除不在窗口內的元素

2. Monotonic queue : O(n)
使用 deque 保存 index，並且保證 deque 中的元素是遞增的
如果新的元素比 deque 中的某些元素大，那麼這些元素永遠不可能成為最大值，因此將其從 deque 中刪除
"""
# @lc code=start
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hp = [(-nums[i], i) for i in range(k)]  # Max Heap，維護窗口內的元素
        heapify(hp)
        ans = [-hp[0][0]]
        for i in range(k, n):
            heappush(hp, (-nums[i], i))
            while hp[0][1] <= i - k:
                heappop(hp)
            ans.append(-hp[0][0])
        return ans

class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # 從大到小的 Monotonic queue, 保存的是 index
        ans = []
        for idx, val in enumerate(nums):
            # 1. 插入，從 tail 移除比 nums[i] 小的數
            while q and nums[q[-1]] <= val:
                q.pop()
            q.append(idx)
            # 2. 維護窗口範圍
            while q[0] <= idx - k:
                q.popleft()
            # 3. 更新答案
            if idx >= k - 1:
                ans.append(nums[q[0]])
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

