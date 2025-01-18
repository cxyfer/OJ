# @algorithm @lc id=3296 lang=python3 
# @title minimum-time-to-revert-word-to-initial-state-ii


from en.Python3.mod.preImport import *
# @test("abacaba",3)=2
# @test("abacaba",4)=1
# @test("abcbabcd",2)=4
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
        i = 1 # 從1開始
        while i * k < n: # 若移除超過n個字元，則必能恢復初始狀態
            if fail[i * k + 1] == i * k: # 若移除後剩下的字元，是否與原字串開頭的字元相同
                return i
            i += 1
        return i