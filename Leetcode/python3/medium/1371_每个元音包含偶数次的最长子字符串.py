#
# @lc app=leetcode.cn id=1371 lang=python3
#
# [1371] 每个元音包含偶数次的最长子字符串
#

# @lc code=start
class Solution:
    """ 異或前綴和
        令 cur << i 為 1 表示第 i 個母音出現奇數次，0 表示出現偶數次。
        若某個狀態的 第 a, b 個母音為 1 ，則要找到另外一個狀態其第 a, b 個母音也為 1 ，兩者間構成的字串才能滿足條件，
        也就是滿足當前狀態的狀態就是自己本身，因此只需保存每個狀態「最早」出現的位置，當再次出現時計算兩者間的距離即可。
    """
    def findTheLongestSubstring(self, s: str) -> int:
        last = dict() # 保存每個狀態「最早」出現的位置
        last[0] = -1 # 空字串
        ans, cur = 0, 0
        for i, ch in enumerate(s):
            idx = "aeiou".find(ch)
            if idx != -1:
                cur ^= 1 << idx
            if cur not in last: # 這個狀態還沒出現過
                last[cur] = i
            else: # 這個狀態出現過，那兩者之間的子串就是符合條件的子串
                ans = max(ans, i - last[cur])
        return ans
# @lc code=end

# @test("eleetminicoworoep")=13
# @test("leetcodeisgreat")=5
# @test("bcbcbc")=6
sol = Solution()
print(sol.findTheLongestSubstring("eleetminicoworoep")) # 13
print(sol.findTheLongestSubstring("leetcodeisgreat")) # 5
print(sol.findTheLongestSubstring("bcbcbc")) # 6