#
# @lc app=leetcode.cn id=3005 lang=python3
#
# [3005] 最大频率元素计数
#
from preImport import *
# @lc code=start
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        return self.solve2(nums)
    def solve1(self, nums: List[int]) -> int: # 兩次遍歷
        cnt = Counter(nums)
        maxCnt = max(cnt.values())
        return sum([v for k, v in cnt.items() if v == maxCnt])
    def solve2(self, nums: List[int]) -> int: # 一次遍歷
        cnt = Counter()
        ans = max_f = 0
        for x in nums:
            cnt[x] += 1
            if cnt[x] > max_f:
                ans = max_f = cnt[x]
            elif cnt[x] == max_f:
                ans += cnt[x]
        return ans
# @lc code=end
sol = Solution()
print(sol.maxFrequencyElements([1,2,2,3,1,4])) # 4
