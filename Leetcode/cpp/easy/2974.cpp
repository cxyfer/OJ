/*
 * @lc app=leetcode.cn id=2974 lang=cpp
 *
 * [2974] 最小数字游戏
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n; i += 2) {
            swap(nums[i], nums[i + 1]);
        }
        return nums;
    }
};
// @lc code=end

