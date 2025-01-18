/*
 * @lc app=leetcode.cn id=1608 lang=cpp
 *
 * [1608] 特殊数组的特征值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int specialArray(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end(), greater<int>());
        for (int i = 1; i <= n; i++){
            // 比 i 大的數至少有 i 個，且比 i 大的數不超過 i 個，即比 i 大的數恰好有 i 個
            if (nums[i-1] >= i && (i == n || nums[i] < i)){
                return i;
            }
        }
        return -1;
    }
};
// @lc code=end

