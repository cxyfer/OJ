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
class Solution1 {
 public:
  vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    int n = candidates.size();
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> ans;
    vector<int> path;
    auto dfs = [&](auto&& dfs, int i, int s) {
      if (s == target) {
        ans.push_back(path);
        return;
      }
      if (i == n) return;
      int x = candidates[i];
      if (s + x > target) return;
      path.push_back(x);
      dfs(dfs, i + 1, s + x);
      path.pop_back();
      while (i < n && candidates[i] == x) {
        i++;
      }
      dfs(dfs, i, s);
    };
    dfs(dfs, 0, 0);
    return ans;
  }
};

class Solution2 {
 public:
  vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    int n = candidates.size();
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> ans;
    vector<int> path;

    auto dfs = [&](auto&& dfs, int i, int s) {
      if (s == target) {
        ans.push_back(path);
        return;
      }
      for (int j = i; j < n; ++j) {
        if (j > i && candidates[j] == candidates[j - 1]) continue;
        if (s + candidates[j] > target) break;
        path.push_back(candidates[j]);
        dfs(dfs, j + 1, s + candidates[j]);
        path.pop_back();
      }
    };
    dfs(dfs, 0, 0);
    return ans;
  }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end