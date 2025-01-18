# # You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.

# # Return an array that consists of indices of peaks in the given array in any order.

# Notes:

# A peak is defined as an element that is strictly greater than its neighboring elements.
# The first and last elements of the array are not a peak.

from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        ans = []
        for i in range(1, n-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                ans.append(i)
        return ans