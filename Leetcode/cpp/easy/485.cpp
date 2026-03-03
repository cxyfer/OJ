/*
 * @lc app=leetcode id=485 lang=cpp
 *
 * [485] Max Consecutive Ones
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n;) {
            while (i < n && nums[i] != 1) i++;
            int j = i;
            while (i < n && nums[i] == 1) i++;
            ans = max(ans, i - j);
        }
        return ans;
    }
};
// @lc code=end

