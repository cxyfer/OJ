/*
 * @lc app=leetcode.cn id=46 lang=cpp
 *
 * [46] 全排列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        // return solve1(nums);
        return solve2(nums);
    }
    vector<vector<int>> solve1(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        vector<int> path(n, 0);
        vector<bool> visited(n, false);
        function<void(int)> dfs = [&](int i) {
            if (i == n) {
                ans.push_back(path);
                return;
            }
            for (int j = 0; j < n; j++) {
                if (!visited[j]) {
                    visited[j] = true;
                    path[i] = nums[j];
                    dfs(i + 1);
                    visited[j] = false;
                }
            }
        };
        dfs(0);
        return ans;
    }
    vector<vector<int>> solve2(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        function<void(int)> perm = [&](int i) {
            if (i == n-1) {
                ans.push_back(nums);
                return;
            }
            for (int j = i; j < n; j++) {
                swap(nums[i], nums[j]);
                perm(i + 1);
                swap(nums[i], nums[j]);
            }
        };
        perm(0);
        return ans;
    }
};
// @lc code=end

