/*
 * @lc app=leetcode.cn id=3011 lang=cpp
 *
 * [3011] 判断一个数组是否可以变为有序
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool canSortArray(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ) {
            int st = i;
            int cnt = __builtin_popcount(nums[i++]);
            while (i < n && __builtin_popcount(nums[i]) == cnt)
                i++;
            sort(nums.begin() + st, nums.begin() + i);
        }
        return is_sorted(nums.begin(), nums.end());
    }
};

class Solution2 {
public:
    bool canSortArray(vector<int>& nums) {
        int n = nums.size();
        int pre = INT_MIN;
        for (int i = 0; i < n;) {
            int mx = nums[i];
            int cnt = __builtin_popcount(nums[i]);
            while (i < n && __builtin_popcount(nums[i]) == cnt) {
                if (nums[i] < pre) return false;
                mx = max(mx, nums[i]);
                i++;
            }
            pre = mx;
        }
        return true;
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end