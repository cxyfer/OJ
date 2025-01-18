// import math
// from typing import *
// from collections import *
// from functools import lru_cache, cache
// from heapq import *
// from bisect import *
// from itertools import *

// class Solution:
//     def isArraySpecial(self, nums: List[int]) -> bool:
//         # n = len(nums)
//         # for i in range(1, n):
//         #     if nums[i] & 1 == nums[i - 1] & 1:
//         #         return False
//         # return True
//         return False if any(nums[i] & 1 == nums[i - 1] & 1 for i in range(1, len(nums))) else True

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            if ((nums[i] & 1) == (nums[i - 1] & 1)) {
                return false;
            }
        }
        return true;
    }
};