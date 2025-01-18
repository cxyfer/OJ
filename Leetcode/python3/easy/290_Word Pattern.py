#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ch2word, word2ch = dict(), dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            if word in word2ch and word2ch[word] != ch:
                return False
            if ch in ch2word and ch2word[ch] != word:
                return False
            word2ch[word] = ch
            ch2word[ch] = word
        return True
# @lc code=end

