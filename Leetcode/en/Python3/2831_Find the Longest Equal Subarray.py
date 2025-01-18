# @algorithm @lc id=2832 lang=python3 
# @title find-the-longest-equal-subarray


# from en.Python3.mod.preImport import *
from collections import Counter
# @test([1,3,2,3,1,3],3)=3
# @test([1,1,2,2,1,1],2)=4
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        # Sliding window, two pointers
        n = len(nums)
        # 購建各元素出現位置的hash table
        pos = [[] for _ in range(n+1)]
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = 0
        for ps in pos:
            # left, right 為窗口的左右邊界，在此遍歷下，index指向的都是相同的元素
            left = 0
            for right, p in enumerate(ps):
                # (p - pos[ps][left] +1) 為目前窗口在原array中的長度
                # (right - left + 1) 為目前窗口內元素ps的數量
                # 兩者相減，即為窗口內非ps元素的數量，也就是需要刪除的元素數量
                while (p - ps[left] +1) - (right - left + 1) > k: # 不符合條件，開始縮小窗口
                    left += 1
                ans = max(ans, right - left + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestEqualSubarray([1,3,2,3,1,3],3)) # 3
    print(sol.longestEqualSubarray([1,1,2,2,1,1],2)) # 4

