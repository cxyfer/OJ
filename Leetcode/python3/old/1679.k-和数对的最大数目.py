#
# @lc app=leetcode.cn id=1679 lang=python3
#
# [1679] K 和数对的最大数目
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution1:
    """
        1. Hash map
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        ans = 0
        for num in nums:
            if cnt[k - num] > 0:
                cnt[k - num] -= 1
                ans += 1
            else:
                cnt[num] += 1
        return ans

class Solution2:
    """
        2. Simple Hash map
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0
        for num in cnt:
            if num * 2 < k: # 避免重複計算，num和k-num只取兩者之間較小的
                ans += min(cnt[num], cnt[k - num])
            elif num * 2 == k:
                ans += cnt[num] // 2
        return ans
    
class Solution(Solution2):
    ...
# @lc code=end

