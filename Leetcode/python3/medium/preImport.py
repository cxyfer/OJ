import sys
import math
import heapq
from typing import *
from collections import *
from functools import *
from operator import *
from string import *

from math import *
from heapq import *
from bisect import *
from itertools import *
from random import *
from sortedcontainers import *

del pow


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def debug(*args, **kwargs):
    print("\033[91m", end="")
    print(*args, **kwargs)
    print("\033[0m", end="")
