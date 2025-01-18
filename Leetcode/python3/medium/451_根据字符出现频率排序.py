#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#
from preImport import *
# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = ""
        for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
            ans += k * v
        return ans
# @lc code=end
# @test("tree")="eert"
# @test("cccaaa")="aaaccc"
# @test("Aabb")="bbAa"
sol = Solution()
print(sol.frequencySort("tree")) # "eert"
print(sol.frequencySort("cccaaa")) # "aaaccc"
print(sol.frequencySort("Aabb")) # "bbAa"
