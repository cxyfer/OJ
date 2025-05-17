/*
 * @lc app=leetcode.cn id=75 lang=cpp
 *
 * [75] 颜色分类
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int i = 0, l = 0, r = n - 1;
        while (i <= r) {
            if (nums[i] == 0) swap(nums[i++], nums[l++]);
            else if (nums[i] == 2) swap(nums[i], nums[r--]);
            else i++;
        }
    }
};
// @lc code=end