/*
 * @lc app=leetcode.cn id=1673 lang=cpp
 *
 * [1673] 找出最具竞争力的子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && st.back() > nums[i] && st.size() + n - i > k) {
                st.pop_back();
            }
            if (st.size() < k) st.push_back(nums[i]);
        }
        return st;
    }
};
// @lc code=end

