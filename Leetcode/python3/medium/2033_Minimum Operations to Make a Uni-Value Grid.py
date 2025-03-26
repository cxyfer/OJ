#
# @lc app=leetcode id=2033 lang=python3
#
# [2033] Minimum Operations to Make a Uni-Value Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minOperations(self, grid: List[List[int]], k: int) -> int:
        arr = [x for row in grid for x in row]
        arr.sort()
        median = arr[len(arr) // 2]
        ans = 0
        for num in arr:
            if abs(num - median) % k != 0:
                return -1
            ans += abs(num - median) // k
        return ans

def select(arr: list[int], k: int, P: int = 5):
    n = len(arr)
    if n <= P:
        arr.sort()
        return arr[k]
    
    chunks = [arr[i:i+P] for i in range(0, n, P)]
    medians = [select(chunk, len(chunk)//2) for chunk in chunks]
    pivot = select(medians, len(medians) // 2)
    
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k < len(left):
        return select(left, k)
    elif k < len(left) + len(equal):
        return pivot
    else:
        return select(right, k - len(left) - len(equal))

class Solution2:
    def minOperations(self, grid: List[List[int]], k: int) -> int:
        arr = [x for row in grid for x in row]
        median = select(arr, len(arr) // 2)
        ans = 0
        for num in arr:
            diff = abs(num - median)
            if diff % k != 0:
                return -1
            ans += diff // k
        return ans

Solution = Solution1
# Solution = Solution2
# @lc code=end

