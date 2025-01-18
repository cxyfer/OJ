# @algorithm @lc id=3297 lang=python3 
# @title minimum-time-to-revert-word-to-initial-state-i


from en.Python3.mod.preImport import *
# @test("abacaba",3)=2
# @test("abacaba",4)=1
# @test("abcbabcd",2)=4
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        i = 1 # 從1開始
        while i * k < n: # 若移除超過n個字元，則必能恢復初始狀態
            if word[i * k:] == word[:n - (i * k)]: # 移除後剩下的字元，是否與原字串開頭的字元相同
                return i
            i += 1
        return i