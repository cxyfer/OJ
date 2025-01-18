#
# @lc app=leetcode id=632 lang=python3
# @lcpr version=30201
#
# [632] Smallest Range Covering Elements from K Lists
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Greedy + Heap
        將問題轉化成從每個list中選一個數，使得這些數的最大值和最小值的差最小
        2. Sliding Window
            a. O(d) 枚舉 mn 和 mx 之間的所有值， d = mx - mn = 2e5
            b. O(n log n) 排序 keys ，只枚舉 keys 中的值， n = 3500 * 50 = 175000

    """
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # return self.solve1(nums)
        # return self.solve2a(nums)
        return self.solve2b(nums)
    def solve1(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        left, right = -float("inf"), float("inf") # answer
        mx = max([nums[i][0] for i in range(n)]) # initial max value
        hp = [(nums[i][0], i, 0) for i in range(n)] # (value, row, col)
        heapq.heapify(hp)
        while True:
            mn, i, j = heapq.heappop(hp) # pop min value
            if mx - mn < right - left: # update answer
                left, right = mn, mx
            if j == len(nums[i]) - 1:
                break
            mx = max(mx, nums[i][j+1]) # update max value
            heapq.heappush(hp, (nums[i][j+1], i, j+1)) # push next value
        return [left, right] 
    def solve2a(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        indices = defaultdict(list) # value -> row
        mn, mx = float("inf"), -float("inf")
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
                mn, mx = min(mn, x), max(mx, x)
        cnt = [0] * n # 每個row分別有幾個數字在窗口內
        inside = 0 # 窗口內涵蓋了幾個row
        l = mn # 窗口左端點
        left, right = mn, mx # answer
        for r in range(mn, mx+1): # 枚舉 [mx, mx] 中的值做為右端點
            if r not in indices: # 右端點不在任何row中，直接跳過
                continue
            for x in indices[r]: # 入窗口
                inside += (cnt[x] == 0)
                cnt[x] += 1
            while inside == n: # 滿足條件，縮小窗口
                if l not in indices: # 左端點不在任何row中，直接跳過
                    l += 1
                    continue
                if r - l < right - left: # 更新答案
                    left, right = l, r
                for x in indices[l]: # 出窗口
                    cnt[x] -= 1
                    inside -= (cnt[x] == 0)
                l += 1
        return [left, right]
    def solve2b(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        indices = defaultdict(list) # value -> row
        mn, mx = float("inf"), -float("inf")
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
                mn, mx = min(mn, x), max(mx, x)
        keys = sorted(indices.keys()) # 枚舉 keys 中的值
        cnt = [0] * n # 每個row分別有幾個數字在窗口內
        inside = 0 # 窗口內涵蓋了幾個row
        il, l = 0, mn # 窗口左端點
        left, right = mn, mx # answer
        for ir, r in enumerate(keys): # 枚舉右端點
            for x in indices[r]: # 入窗口
                inside += (cnt[x] == 0)
                cnt[x] += 1
            while inside == n: # 滿足條件，縮小窗口
                l = keys[il]
                if r - l < right - left: # 更新答案
                    left, right = l, r
                for x in indices[l]: # 出窗口
                    cnt[x] -= 1
                    inside -= (cnt[x] == 0)
                il += 1
        return [left, right]
# @lc code=end



#
# @lcpr case=start
# [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[1,2,3],[1,2,3]]\n
# @lcpr case=end

#

