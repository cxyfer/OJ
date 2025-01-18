// import math
// from typing import *
// from collections import *
// from functools import *
// from heapq import *
// from bisect import *
// from itertools import *

// class Solution:
//     def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
//         MOD = 10**9 + 7
//         n = len(nums)
//         ans = 0
//         def helper():
//             if n == 1:
//                 return max(0, nums[0])
//             dp = [0] * n
//             dp[0] = max(0, nums[0])
//             if n > 1:
//                 dp[1] = max(dp[0], nums[1])
//             for i in range(2, n):
//                 dp[i] = max(dp[i-1], dp[i-2] + nums[i])
//             return dp[-1]
//         for pos, x in queries:
//             nums[pos] = x
//             ans = (ans + helper()) % MOD
//         return ans

// sol = Solution()
// print(sol.maximumSumSubsequence([3,5,9], [[1,-2],[0,-3]])) # 21
// print(sol.maximumSumSubsequence([0,-1], [[0,-5]])) # 0
// print(sol.maximumSumSubsequence([6], [[0,-2]])) # 0

#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;
class Solution {
public:
    int maximumSumSubsequence(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int ans = 0;
        vector<int> dp(max(n, 2));
        dp[0] = max(0, nums[0]);
        if (n > 1) dp[1] = max(dp[0], nums[1]);
        for (int i = 2; i < n; i++) dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        for (auto& query : queries) {
            int pos = query[0], x = query[1];
            nums[pos] = x;
            if (pos == 0){
                dp[0] = max(0, nums[0]);
                if (n > 1) dp[1] = max(dp[0], nums[1]);
            }
            else if (pos == 1) dp[1] = max(dp[0], nums[1]);
            for (int i = max(2, pos); i < n; i++) {
                dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
            }
            ans = (ans + dp[n-1]) % MOD;
        }
        return ans;
    }
};
