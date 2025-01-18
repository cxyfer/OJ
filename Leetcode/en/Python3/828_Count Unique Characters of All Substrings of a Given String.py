# @algorithm @lc id=855 lang=python3 
# @title count-unique-characters-of-all-substrings-of-a-given-string


from en.Python3.mod.preImport import *
# @test("ABC")=10
# @test("ABA")=8
# @test("LEETCODE")=92
class Solution:
    """
        分別計算每個字母的貢獻度
        https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/solutions/1804194/tong-ji-zi-chuan-zhong-de-wei-yi-zi-fu-b-ajio/
    """
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        last = [-1] * 26 # 上一個字母出現的位置
        cur = [-1] * 26 # 當前字母出現的位置

        ans = 0
        for i, ch in enumerate(s):
            index = ord(ch) - ord('A')
            # 若cur的索引不是-1(當前字母出現過2次以上)，計算貢獻度
            if cur[index] > -1:
                ans += (i - cur[index]) * (cur[index] - last[index])
            # 滾動存放cur和last
            last[index] = cur[index]
            cur[index] = i
        # 計算最後一個字母的貢獻度
        for index in range(26):
            if cur[index] > -1:
                ans += (cur[index] - last[index]) * (len(s) - cur[index])
        return ans
