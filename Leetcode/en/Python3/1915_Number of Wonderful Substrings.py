# @algorithm @lc id=2044 lang=python3 
# @title number-of-wonderful-substrings


from en.Python3.mod.preImport import *
# @test("aba")=4
# @test("aabb")=9
# @test("he")=2
class Solution:
    """
        前綴和 + 狀態壓縮

        s << i 表示第 i 個字元是否出現奇數次
        cnt[s] 表示前綴和 s 出現的次數

        > 這題真的不是 Hard ?
    """
    def wonderfulSubstrings(self, word: str) -> int:
        # cnt = Counter([0]) # 前綴和出現次數，初始化為0
        cnt = [0] * (1 << 10) # 前綴和出現次數，初始化為0
        cnt[0] = 1 # 空字串
        s = 0
        ans = 0
        for ch in word:
            idx = ord(ch) - ord('a') # 當前字元的索引
            s ^= (1 << idx) # 反轉當前字元的出現次數
            ans += cnt[s] # 只有 s 自身滿足和 s 兩個狀態間所有字元的出現次數都是偶數，即 s ^ s = 0
            ans += sum(cnt[s ^ (1 << i)] for i in range(10)) # 其中一個字元出現次數是奇數，即 s ^ (s ^ (1 << i)) 只有 1 個 1
            cnt[s] += 1 # 更新前綴和出現次數
        return ans