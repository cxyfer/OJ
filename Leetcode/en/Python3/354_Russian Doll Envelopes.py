# @algorithm @lc id=354 lang=python3 
# @title russian-doll-envelopes


from en.Python3.mod.preImport import *
# @test([[5,4],[6,4],[6,7],[2,3]])=3
# @test([[1,1],[1,1],[1,1]])=1
class Solution:
    """
        Longest Increasing Subsequence (LIS)
        DP 會超時，因此使用 Greedy + Binary Search
    """
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1])) # 先按照寬度升序排列，若寬度相同，則按照「高度降序」排列
        n = len(envelopes)
        tail = [envelopes[0]] # tail[i] 表示 長度為 i+1 的 LIS 的最後一個元素的最小值，初始化 tail[0] = nums[0]
        for i in range(1, n):
            if envelopes[i][0] > tail[-1][0] and envelopes[i][1] > tail[-1][1]: # nums[i] 可以接在 tail 的末尾，並構成更長的 LIS
                tail.append(envelopes[i]) # tail 長度加 1
                continue

            # 在 tail 中二分查找，找到第一個大於等於 nums[i] 的元素，並將其更新為 nums[i]
            left = 0
            right = len(tail) - 1
            while left <= right: # [left, right]
                mid = (left + right) // 2
                if tail[mid][0] < envelopes[i][0] and tail[mid][1] < envelopes[i][1]:
                    left = mid + 1
                else:
                    right = mid -1
            tail[left] = envelopes[i]
        return len(tail)