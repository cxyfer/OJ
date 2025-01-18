// # import math
// # from typing import *
// # from collections import *
// # from functools import lru_cache, cache
// # from heapq import *
// # from bisect import *
// # from itertools import *

// # class Solution:
// #     def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
// #         n = len(nums)
// #         special = [0] * n
// #         for i in range(1, n):
// #             if nums[i] & 1 == nums[i - 1] & 1:
// #                 special[i] = 1
// #         s = list(accumulate(special)) # prefix sum
// #         ans = []
// #         for l, r in queries:
// #             ans.append(True if s[r] - s[l] == 0 else False)
// #         return ans

// # sol = Solution()
// # # print(sol.isArraySpecial([3,4,1,2,6], [[0,4]])) # [False]
// # # print(sol.isArraySpecial([4,3,1,6], [[0,2],[2,3]])) # [False, True]

// # print(sol.isArraySpecial([3,3,1,2,6], [[0,2]])) # [False]

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> special(n);
        for (int i = 1; i < n; i++) {
            if ((nums[i] & 1) == (nums[i - 1] & 1)) special[i] = 1;
        }
        vector<int> s(n);
        for (int i = 1; i < n; i++) {
            s[i] = s[i - 1] + special[i];
        }
        vector<bool> ans;
        for (auto& q: queries) {
            int l = q[0], r = q[1];
            ans.push_back(s[r] - s[l] == 0);
        }
        return ans;
    }
};