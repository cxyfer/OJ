import sys
import math
import heapq
from typing import *
from collections import *
from functools import *
from operator import *
from string import *
del pow

from heapq import *
from bisect import *
from itertools import *
from random import *
from sortedcontainers import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right