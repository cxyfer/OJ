import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        flag = 0
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            flag ^= 1
        return "Alice" if flag != 0 else "Bob"