/*
 * @lc app=leetcode.cn id=3194 lang=cpp
 *
 * [3194] 最小元素和最大元素的最小平均值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    double minimumAverage(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        double ans = FLT_MAX;
        int left = 0, right = n - 1;
        while (left < right) {
            ans = min(ans, (nums[left++] + nums[right--]) / 2.0);
        }
        return ans;
    }
};

class Solution2 {
public:
    double minimumAverage(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int ans = nums[0] + nums[n - 1];
        for (int i = 1; i < n / 2; i++) {
            ans = min(ans, nums[i] + nums[n - 1 - i]);
        }
        return ans / 2.0;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

