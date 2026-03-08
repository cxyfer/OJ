/*
 * @lc app=leetcode.cn id=1980 lang=cpp
 *
 * [1980] 找出不同的二进制字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        int n = nums.size();
        string ans(n, '0');
        for (auto const [i, num] : views::enumerate(nums))
            ans[i] = num[i] == '0' ? '1' : '0';
        return ans;
    }
};
// @lc code=end

