# @algorithm @lc id=1567 lang=python3 
# @title maximum-number-of-vowels-in-a-substring-of-given-length


from en.Python3.mod.preImport import *
# @test("abciiidef",3)=3
# @test("aeiou",2)=2
# @test("leetcode",3)=2
class Solution:
    """
        Sliding window
    """
    def maxVowels(self, s: str, k: int) -> int:
        ans = cur = sum(1 for ch in s[:k] if ch in 'aeiou')
        for idx in range(k, len(s)):
            if s[idx] in 'aeiou':
                cur += 1
            if s[idx-k] in 'aeiou':
                cur -= 1
            ans = max(ans, cur)
        return ans