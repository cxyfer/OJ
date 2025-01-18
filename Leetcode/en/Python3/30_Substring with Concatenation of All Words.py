# @algorithm @lc id=30 lang=python3 
# @title substring-with-concatenation-of-all-words


from en.Python3.mod.preImport import *
# @test("barfoothefoobarman",["foo","bar"])=[0,9]
# @test("wordgoodgoodgoodbestword",["word","good","best","word"])=[]
# @test("barfoofoobarthefoobarman",["bar","foo","the"])=[6,9,12]
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # return self.solve1(s, words)
        return self.solve2(s, words)
    """
        1. Hash Table
    """
    def solve1(self, s: str, words: List[str]) -> List[int]:
        n, m, w = len(s), len(words), len(words[0])
        cnt = Counter(words)
        ans = []
        for i in range(n - m * w + 1): # 長度為 m * w
            cur = Counter([s[j:j + w] for j in range(i, i + m * w, w)])
            if cur == cnt:
                ans.append(i)
        return ans
    """
        2. Hash Table + Sliding Window
    """
    def solve2(self, s: str, words: List[str]) -> List[int]:
        n, m, w = len(s), len(words), len(words[0])
        cnt = Counter(words)
        ans = []
        for i in range(w): # 從0~w-1開始，每次移動w個位置
            cur = Counter()
            for j in range(i, n - w + 1, w):
                if j >= i + m * w: # 出窗口
                    w_out = s[j - m * w:j - m * w + w]
                    if cur[w_out] == 1:
                        del cur[w_out]
                    else:
                        cur[w_out] -= 1
                w_in = s[j:j + w]
                cur[w_in] += 1
                if cur == cnt:
                    ans.append(j - (m - 1) * w)
        return ans
