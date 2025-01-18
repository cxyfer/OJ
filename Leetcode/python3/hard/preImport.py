import math
from typing import *
from collections import *
from sortedcontainers import *
from functools import lru_cache
from heapq import *
from bisect import *
from itertools import *
from atcoder.fenwicktree import FenwickTree
from atcoder.segtree import SegTree

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