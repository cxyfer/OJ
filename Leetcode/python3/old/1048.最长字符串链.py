#
# @lc app=leetcode.cn id=1048 lang=python3
#
# [1048] 最长字符串链
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 由短到長排序，對每個word找所有比它短一個字母的word，從其中取最長鏈最長的，更新最長鏈
        words.sort(key=len)
        dic = {}
        for s in words:
            res = 0
            for i in range(len(s)):
                cur = s[:i] + s[i+1:] # 去掉s[i]
                res = max(res, dic.get(cur, 0))
            dic[s] = res + 1
        return max(dic.values())
# @lc code=end

