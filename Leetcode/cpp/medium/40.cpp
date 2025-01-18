/*
 * @lc app=leetcode.cn id=40 lang=cpp
 *
 * [40] 组合总和 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        int n = candidates.size();
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> ans;
        vector<int> path;
        function<void(int, int)> dfs = [&](int i, int s) {
            if (s == target) {
                ans.push_back(path);
                return;
            }
            for (int j = i; j < n; ++j) {
                if (j > i && candidates[j] == candidates[j - 1]) continue;
                if (s + candidates[j] > target) break;
                path.push_back(candidates[j]);
                dfs(j + 1, s + candidates[j]);
                path.pop_back();
            }
        };
        dfs(0, 0);
        return ans;
    }
};
// @lc code=end