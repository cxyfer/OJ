import math
from math import *
from typing import *
from collections import *
from functools import lru_cache
import heapq
from heapq import *
from bisect import *
from itertools import *

def cache(user_function):
    return lru_cache(maxsize=None)(user_function)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right