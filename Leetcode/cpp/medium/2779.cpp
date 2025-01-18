/*
 * @lc app=leetcode.cn id=2779 lang=cpp
 *
 * [2779] 数组的最大美丽值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int ans = 0, left = 0;
        for (int right = 0; right < n; right++) { // 枚舉右端點
            while (nums[right] - nums[left] > k * 2) { // 保證窗口內最大值和最小值之差不超過2k
                left++;
            }
            ans = max(ans, right - left + 1); // 更新答案
        }
        return ans;
    }
};

class Solution2 {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        int mx = *max_element(nums.begin(), nums.end());
        vector<int> diff(mx + 2);
        for (int x : nums) {
            diff[max(x - k, 0)]++;
            diff[min(x + k + 1, mx + 1)]--;
        }
        int ans = 0, s = 0;
        for (int x : diff) {
            s += x;
            ans = max(ans, s);
        }
        return ans;
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};

// @lc code=end