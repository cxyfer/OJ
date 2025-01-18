/*
 * @lc app=leetcode.cn id=3159 lang=cpp
 *
 * [3159] 查询数组中元素的出现位置
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
        int n = nums.size();
        vector<int> pos, ans;
        for (int i = 0; i < n; i++) if (nums[i] == x) pos.push_back(i);
        for (int q : queries) ans.push_back(q <= pos.size() ? pos[q - 1] : -1);
        return ans;
    }
};
// @lc code=end

