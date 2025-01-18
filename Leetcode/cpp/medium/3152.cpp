/*
 * @lc app=leetcode.cn id=3152 lang=cpp
 *
 * [3152] Special Array II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> special(n, 0);
        for (int i = 1; i < n; i++) {
            if ((nums[i] & 1) == (nums[i - 1] & 1)) special[i] = 1;
        }
        vector<int> s(n, 0); // prefix sum
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
// @lc code=end

