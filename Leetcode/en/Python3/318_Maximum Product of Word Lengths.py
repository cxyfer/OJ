# @algorithm @lc id=318 lang=python3 
# @title maximum-product-of-word-lengths


from en.Python3.mod.preImport import *
# @test(["abcw","baz","foo","bar","xtfn","abcdef"])=16
# @test(["a","ab","abc","d","cd","bcd","abcd"])=4
# @test(["a","aa","aaa","aaaa"])=0
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n # 紀錄words[i]出現過的字母
        for idx, w in enumerate(words):
            tmp = 0
            for ch in w:
                tmp |= (1 << (ord(ch) - ord('a')))
            masks[idx] = tmp
            idx += 1
        ans = 0
        for i in range(n):
            for j in range(i):
                if masks[i] & masks[j] == 0: # no common letters
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans