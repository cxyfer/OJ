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
        int l = 0, r = n - 1, idx = 0;
        while (idx <= r) {
            if (nums[idx] == 0)
                swap(nums[l++], nums[idx++]);
            else if (nums[idx] == 2) // 注意這裡 idx 不能 +1
                swap(nums[r--], nums[idx]);  
            else
                idx++;
        }
    }
};
// @lc code=end