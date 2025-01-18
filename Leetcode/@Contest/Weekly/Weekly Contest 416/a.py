import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        st = set(bannedWords)
        cnt = 0
        for word in message:
            if word in st:
                cnt += 1
                if cnt >= 2:
                    return True
        return False
