# @algorithm @lc id=2755 lang=python3 
# @title extra-characters-in-a-string


from en.Python3.mod.preImport import *
# @test("leetscode",["leet","code","leetcode"])=1
# @test("sayhelloworld",["hello","world"])=3
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        n = len(s)
        @cache
        def dfs(i: int) -> int:
            if i < 0: return 0
            res = dfs(i - 1) + 1  # 不選此字母，即令此字母為額外字母，獨自成為一個單詞
            for j in range(i + 1): # 遍歷所有可能的前綴，計算其額外字母數量
                if s[j:i + 1] in words:
                    res = min(res, dfs(j - 1))
            return res
        return dfs(n - 1)

