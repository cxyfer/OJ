/*
 * @lc app=leetcode.cn id=3040 lang=cpp
 *
 * [3040] 相同分数的最大操作数目 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxOperations(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        vector<vector<int>> memo(n, vector<int>(n));
        auto helper = [&](int i, int j, int target) -> int {
            for (auto& row : memo) fill(row.begin(), row.end(), -1); // 初始化為 -1
            function<int(int, int)> dfs = [&](int i, int j) -> int {
                if (i >= j) return 0;
                if (memo[i][j] != -1) return memo[i][j];
                int res = 0;
                if (nums[i] + nums[i + 1] == target) res = max(res, 1 + dfs(i + 2, j));
                if (nums[j - 1] + nums[j] == target) res = max(res, 1 + dfs(i, j - 2));
                if (nums[i] + nums[j] == target) res = max(res, 1 + dfs(i + 1, j - 1));
                return memo[i][j] = res;
            };
            return dfs(i, j);
        };
        ans = max(ans, helper(2, n - 1, nums[0] + nums[1]));
        ans = max(ans, helper(0, n - 3, nums[n - 2] + nums[n - 1]));
        ans = max(ans, helper(1, n - 2, nums[0] + nums[n - 1]));
        return ans + 1;
    }
};
// @lc code=end

// class Solution:
//     def maxOperations(self, nums: List[int]) -> int:
//         n = len(nums)
//         @cache
//         def dfs(target, i, j): # (目標值, 左邊界, 右邊界)
//             if i >= j: # 區間內的數字小於2個
//                 return 0
//             res = 0
//             if nums[i] + nums[i+1] == target: # 使用左邊的兩個數字
//                 res = max(res, 1 + dfs(target, i+2, j))
//             if nums[j-1] + nums[j] == target: # 使用右邊的兩個數字
//                 res = max(res, 1 + dfs(target, i, j-2))
//             if nums[i] + nums[j] == target: # 使用左右各一個數字
//                 res = max(res, 1 + dfs(target, i+1, j-1))
//             return res
//         res1 = dfs(nums[0] + nums[1], 2, n-1) # 使用左邊的兩個數字當作目標值
//         res2 = dfs(nums[-2] + nums[-1], 0, n-3) # 使用右邊的兩個數字當作目標值
//         res3 = dfs(nums[0] + nums[-1], 1, n-2) # 使用左右各一個數字之和當作目標值
//         return 1 + max(res1, res2, res3)