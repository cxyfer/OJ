# @algorithm @lc id=1281 lang=python3 
# @title can-make-palindrome-from-substring


from en.Python3.mod.preImport import *
# @test("abcda",[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]])=[true,false,false,true,true]
# @test("lyb",[[0,1,0],[2,2,1]])=[false,true]
class Solution:
    """ 樸素前綴和 / 異或前綴和
        由於可以重新排列以及替換 k 個字元，因此我們只需關心區間內每個字母的出現次數的奇偶性即可。
        - 出現次數偶數的字母不需要替換，重新排列到回文字串的兩側即可。
        - 出現次數奇數的字母需要替換，有以下兩種情況，為方便令 m 為區間內奇數次數的字母個數：
            - 字串長度為奇數，即有奇數個字母出現奇數次，此時可以替換 (m-1)/2 個字母
            - 字串長度為偶數，即有偶數個字母出現奇數次，此時可以替換 m/2 個字母
          不管哪種情況，都需替換 floor(m/2) 個字母
    """
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # return self.solve1(s, queries)
        return self.solve2(s, queries)
    """
        1. 樸素前綴和
        紀錄每個字母出現次數的前綴和，再根據區間內的字母出現次數奇偶性計算 m，最後判斷是否可以替換。
        Time: O((n+q)*26)
    """
    def solve1(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        cnt = [[0 for _ in range(26)] for _ in range(n + 1)]
        for i, ch in enumerate(s):
            cnt[i + 1] = cnt[i].copy()
            cnt[i + 1][ord(ch) - ord('a')] += 1
        ans = []
        for l, r, k in queries:
            m = sum((cnt[r + 1][i] - cnt[l][i]) & 1 for i in range(26)) # 奇數次數的字母個數
            ans.append(m // 2 <= k) # 替換次數是否足夠
        return ans
    """
        2. 異或前綴和
        由於我們只關心每種字母出現次數的奇偶性，因此可以用位運算來保存每種字母出現次數的奇偶性。
        令 1 表示奇數次數，0 表示偶數次數，則區間內的字母出現次數奇偶性可以用一個 26 位的二進制數表示。
        只有 奇數-偶數=奇數 和 偶數-奇數=奇數 這兩種情況會出現奇數次數的字母，用位運算表示就是 1 ^ 0 = 1 和 0 ^ 1 = 1。
        Time: O(n+q)
    """
    def solve2(self, s: str, queries: List[List[int]]) -> List[bool]:
        xors = [0] # XOR Prefix Sum
        for ch in s:
            b = 1 << (ord(ch) - ord('a')) # 1 << i 表示第 i 個字母
            xors.append(xors[-1] ^ b)  # 奇數變偶數，偶數變奇數
        ans = []
        for left, right, k in queries:
            m = (xors[left] ^ xors[right + 1]).bit_count() # 奇數次數的字母個數
            ans.append(m // 2 <= k)
        return ans