#
# @lc app=leetcode id=1813 lang=python3
# @lcpr version=30204
#
# [1813] Sentence Similarity III
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        tokens1, tokens2 = sentence1.split(), sentence2.split()
        if len(tokens1) > len(tokens2):
            tokens1, tokens2 = tokens2, tokens1
        n, m = len(tokens1), len(tokens2)
        i = j = 0
        while i < n and tokens1[i] == tokens2[i]:
            i += 1
        while j < n - i and tokens1[n - 1 - j] == tokens2[m - 1 - j]:
            j += 1
        return i + j == n
# @lc code=end

sol = Solution()
print(sol.areSentencesSimilar("My name is Haley", "My Haley")) # True
print(sol.areSentencesSimilar("of", "A lot of words")) # False
print(sol.areSentencesSimilar("Eating right now", "Eating")) # True


#
# @lcpr case=start
# "My name is Haley"\n"My Haley"\n 
# @lcpr case=end

# @lcpr case=start
# "of"\n"A lot of words"\n
# @lcpr case=end

# @lcpr case=start
# "Eating right now"\n"Eating"\n
# @lcpr case=end

#

