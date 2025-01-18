import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1: return word
        if numFriends == n: return max(word)

        L_max = n - numFriends + 1
        ans = ""
        for i in range(n):
            ans = max(ans, word[i:i + min(n - i, L_max)])
        return ans
    
sol = Solution()
print(sol.answerString("dbca", 2)) # "dbc"
print(sol.answerString("gggg", 4)) # "g"

# Example 1:

# Input: word = "dbca", numFriends = 2

# Output: "dbc"

# Explanation: 

# All possible splits are:

# "d" and "bca".
# "db" and "ca".
# "dbc" and "a".
# Example 2:

# Input: word = "gggg", numFriends = 4

# Output: "g"

# Explanation: 

# The only possible split is: "g", "g", "g", and "g".

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.©leetcode
