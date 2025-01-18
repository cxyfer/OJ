#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#
from preImport import *
# @lc code=start
class Solution:
    """
        將問題轉化為：求長度為n-k的連續子數組的最小和
        1. Prefix Sum
        2. Sliding Window
    """
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # return self.solve1(cardPoints, k)
        return self.solve2(cardPoints, k)

    def solve1(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        pre_sum = list(accumulate(cardPoints, initial=0))
        mn = float('inf')
        for i in range(k+1):
            mn = min(mn, pre_sum[i+(n-k)] - pre_sum[i])
        return sum(cardPoints) - mn
    
    def solve2(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left, right = 0, n - k
        ans = cur = sum(cardPoints[left:right])
        for _out, _in in zip(cardPoints, cardPoints[right:]):
            cur += _in - _out
            ans = min(ans, cur)
        return sum(cardPoints) - ans
# @lc code=end
sol = Solution()
print(sol.maxScore([1,2,3,4,5,6,1],3)) # 12
print(sol.maxScore([2,2,2],2)) # 4
print(sol.maxScore([9,7,7,9,7,7,9],7)) # 55
