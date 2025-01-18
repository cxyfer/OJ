import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

    
solution = Solution()  
print(solution.validSequence("vbcca", "abc"))  # 輸出: [0, 1, 2]  
print(solution.validSequence("bacdc", "abc"))  # 輸出: [1, 2, 4]  
print(solution.validSequence("aaaaaa", "aaabc"))  # 輸出: []  
print(solution.validSequence("abc", "ab"))  # 輸出: [0, 1]
print(solution.validSequence("aaaaaa", "aaabc"))  # 輸出: []
