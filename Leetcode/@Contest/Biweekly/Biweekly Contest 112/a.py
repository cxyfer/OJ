import math
from math import *
from typing import *
from collections import *

"""
7021. Check if Strings Can be Made Equal With Operations I

You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.
"""

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if Counter(s1) != Counter(s2):
            return False
        list1 = list(s1)[:]
        list2 = list(s1)[:]
        list3 = list(s1)[:]
        list1[0], list1[2] = list1[2], list1[0]
        list2[1], list2[3] = list2[3], list2[1]
        list3[0], list3[2] = list3[2], list3[0]
        list3[1], list3[3] = list3[3], list3[1]
        #print(list1, list2, list3)
        return s2 == "".join(list1) or s2 == "".join(list2) or s2 == "".join(list3)
sol = Solution()
print(sol.canBeEqual("abcd", "cdab"))
print(sol.canBeEqual("abcd", "dcba"))