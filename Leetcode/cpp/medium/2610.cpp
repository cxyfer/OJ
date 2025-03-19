/*
 * @lc app=leetcode.cn id=2610 lang=cpp
 * @lcpr version=30204
 *
 * [2610] 转换二维数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        int mx = 0;
        unordered_map<int, int> cnt;
        for (int x : nums) mx = max(mx, ++cnt[x]);
        vector<vector<int>> ans(mx);
        for (auto& [x, v] : cnt)
            for (int i = 0; i < v; i++)
                ans[i].push_back(x);
        return ans;
    }
};

class Solution2 {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        int n = nums.size();
        vector<int> cnt(n + 1);
        vector<vector<int>> ans;
        for (int x : nums) {
            if (cnt[x] == ans.size()) {
                ans.emplace_back();
            }
            ans[cnt[x]++].emplace_back(x);
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end



/*
// @lcpr case=start
// [1,3,4,1,2,3,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4]\n
// @lcpr case=end

 */

