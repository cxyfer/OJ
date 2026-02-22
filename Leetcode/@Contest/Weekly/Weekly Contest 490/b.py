import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        ans = 0
        t = n
        while t:
            t, x = divmod(t, 10)
            ans += math.factorial(x)
        return sorted(str(ans)) == sorted(str(n))


sol = Solution()
print(sol.isDigitorialPermutation(415))
