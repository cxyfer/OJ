// import math
// from typing import *
// from collections import *
// from functools import *
// from heapq import *
// from bisect import *
// from itertools import *

// class Solution:
//     def maximumTotalCost(self, nums: List[int]) -> int:
//         n = len(nums)
//         s1, s2 = [0] * (n + 1), [0] * (n + 1)
//         for i, x in enumerate(nums):
//             s1[i + 1] = s1[i] + x * (1 if 1 & i else -1)
//             s2[i + 1] = s2[i] + x * (-1 if 1 & i else 1)

//         @cache
//         def cost(i: int, j: int) -> int:
//             return s1[j+1] - s1[i] if i & 1 else s2[j+1] - s2[i]
        
//         @cache
//         def dfs(i):
//             if i == n:
//                 return 0
//             return max(cost(i, j) + dfs(j + 1) for j in range(i, n))

//         return dfs(0)

// sol = Solution()
// print(sol.maximumTotalCost([1,-2,3,4])) # 10
// print(sol.maximumTotalCost([1,-1,1,-1])) # 4
// print(sol.maximumTotalCost([0])) # 0
// print(sol.maximumTotalCost([1,-1])) #2

using LL = long long;

class Solution {
public:
    long long maximumTotalCost(vector<int>& nums) {
        int n = nums.size();
        vector<LL> s1(n + 1), s2(n + 1);
        for (int i = 0; i < n; i++) {
            s1[i + 1] = s1[i] + nums[i] * (1 & i ? -1 : 1);
            s2[i + 1] = s2[i] + nums[i] * (1 & i ? 1 : -1);
        }

        function<LL(int, int)> cost = [&](int i, int j) {
            return i & 1 ? s2[j + 1] - s2[i] : s1[j + 1] - s1[i];
        };

        vector<LL> dp(n + 1, LLONG_MIN);
        dp[n] = 0;
        vector<pair<LL, int>> mx(n + 1);
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                dp[i] = max(dp[i], cost(i, j) + dp[j + 1]);
            }
        }
        return dp[0];
    }
};

        // dp = [-float("inf")] * (n + 1)
        // dp[n] = 0
        // mx = [(0, i-1) for i in range(n + 1)]
        // for i in range(n - 1, -1, -1):
        //     mx_j = -1
        //     for j in range(i, n):
        //         if cost(i, j) + dp[j + 1] > dp[i]:
        //             dp[i] = cost(i, j) + dp[j + 1]
        //             mx_j = j
        //         # dp[i] = max(dp[i], cost(i, j) + dp[j + 1])
        //     print(i, dp[mx_j + 1], mx_j)
        // print(dp)