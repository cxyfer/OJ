from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from string import *
from typing import *


class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def convert(t: str):
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s
        return convert(endTime) - convert(startTime)
