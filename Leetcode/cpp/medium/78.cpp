/*
 * @lc app=leetcode.cn id=78 lang=cpp
 *
 * [78] 子集
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int kase = 1;
        if (kase == 1) return solve1(nums);
        else if (kase == 2) return solve2(nums);
        else if (kase == 3) return solve3(nums);
        else return solve3(nums);
        // return solve1(nums);
        // return solve2(nums);
        // return solve3(nums);
    }
    vector<vector<int>> solve1(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        vector<int> path;
        function<void(int)> dfs = [&](int i) {
            if (i == n) {             // 到達葉節點
                ans.push_back(path);  // Array 沒有 Reference 問題
                return;
            }
            dfs(i + 1);  // 不選 nums[i]
            path.push_back(nums[i]);
            dfs(i + 1);  // 選 nums[i]
            path.pop_back();
        };
        dfs(0);
        return ans;
    }
    vector<vector<int>> solve2(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        for (int i = 0; i < (1 << n); i++) {  // 枚舉所有子集，狀態壓縮
            vector<int> cur;                  // 當前子集
            for (int j = 0; j < n; j++) {  // 檢查 nums[j] 是否在當前子集中
                if (i & (1 << j)) cur.push_back(nums[j]);
            }
            ans.push_back(cur);
        }
        return ans;
    }
    vector<vector<int>> solve3(vector<int>& nums) {
        vector<vector<int>> ans = {{}};  // 初始化答案，只包含一個空集合
        for (int x : nums) {             // 枚舉所有元素
            int k = ans.size();
            for (int j = 0; j < k; j++) {
                vector<int> cur = ans[j];
                cur.push_back(x);
                ans.push_back(cur);
            }
        }
        return ans;
    }
};
// @lc code=end

