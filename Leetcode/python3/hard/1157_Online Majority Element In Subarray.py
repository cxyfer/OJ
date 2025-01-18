#
# @lc app=leetcode id=1157 lang=python3
# @lcpr version=30204
#
# [1157] Online Majority Element In Subarray
#


# @lcpr-template-start
from preImport import *
from random import *
# @lcpr-template-end
# @lc code=start
"""
    1. Random Sampling + Binary Search
    Suppose x is the majority element, then probablity of x is greater than 1/2.

    Random sampling k times, the probablity of correct answer is greater than 1 - 1/2^k.
    for all q times query, the probablity of correct answer is greater than (1 - 1/2^k)^q ~= 1 - q * 1/2^k.

    When q = 10^4, k = 20, the probablity of correct answer is about 99%

    Time Complexity: O(n + q * k * logn)
    Space Complexity: O(n)
"""
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.k = 20 # 20 times random sampling
        self.arr = arr
        self.pos = defaultdict(list)
        for i, x in enumerate(arr):
            self.pos[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        arr = self.arr
        pos = self.pos
        for _ in range(self.k):
            x = arr[randint(left, right)] # random sampling x
            cnt = bisect_left(pos[x], right + 1) - bisect_left(pos[x], left) # count of x in arr[left:right]
            if cnt >= threshold:
                return x
            elif cnt * 2 >= right - left + 1: # x is the majority element, but not enough threshold
                return -1
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end

obj = MajorityChecker([1,1,2,2,1,1])
print(obj.query(0,5,4)) # 1
print(obj.query(0,3,3)) # -1
print(obj.query(2,3,2)) # 2

# MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // 返回 1
# majorityChecker.query(0,3,3); // 返回 -1
# majorityChecker.query(2,3,2); // 返回 2


