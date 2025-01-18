#
# @lc app=leetcode.cn id=3029 lang=python3
#
# [3029] 将单词恢复初始状态所需的最短时间 I
#
from preImport import *
# @lc code=start
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        # KMP
        fail = [0] * (n + 1)
        for i in range(1, n):
            j = fail[i]
            while j and word[i] != word[j]:
                j = fail[j]
            fail[i + 1] = j + (word[i] == word[j])
        print(fail)
        i = 1 # 從1開始
        while i * k < n: # 若移除超過n個字元，則必能恢復初始狀態
            print(word[i * k:], word[:n - (i * k)])
            print(fail[n] , n-i*k)
            if fail[n] == n-i*k: # 若移除後剩下的字元，是否與原字串開頭的字元相同
                return i
            i += 1
        return i
# @lc code=end
sol = Solution()
print(sol.minimumTimeToInitialState("abacaba",3)) # 2
# print(sol.minimumTimeToInitialState("abacaba",4)) # 1
# print(sol.minimumTimeToInitialState("abcbabcd",2)) # 4
# print(sol.minimumTimeToInitialState("baba",3)) # 2