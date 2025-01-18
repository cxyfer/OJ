import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            for d in range(9, 0, -1):
                if d % k == 0:
                    return str(d)
            return ""

        def generatePalindrome(half: str, length: int) -> str:
            if length % 2 == 0:
                return half + half[::-1]
            else:
                return half + half[-2::-1]
            
        half = '9' * ((n + 1) // 2)
        ans = generatePalindrome(half, n)
        
        while int(ans) % k != 0:
            half = list(half)
            i = len(half) - 1
            while i >= 0 and half[i] == '0':
                half[i] = '9'
                i -= 1
            if i >= 0:
                half[i] = chr(ord(half[i]) - 1)
            else:
                return ""
            half = ''.join(half).lstrip('0')
            ans = generatePalindrome(half, n)

        return ans

sol = Solution()
print(sol.largestPalindrome(3, 5)) # 595
print(sol.largestPalindrome(1, 4)) # 8
print(sol.largestPalindrome(5, 6)) # 89898