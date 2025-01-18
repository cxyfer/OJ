/*
 * @lc app=leetcode.cn id=945 lang=cpp
 *
 * [945] 使数组唯一的最小增量
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        // return solve1(nums);
        // return solve2a(nums);
        return solve2b(nums);
    }
    int solve1(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        sort(nums.begin(), nums.end());
        for (int i = 1; i < n; i++) {
            if (nums[i] <= nums[i-1]) {
                ans += nums[i-1] + 1 - nums[i];
                nums[i] = nums[i-1] + 1;
            }
        }
        return ans;
    }
    int solve2a(vector<int>& nums) {
        int n = nums.size(), mx = *max_element(nums.begin(), nums.end());
        vector<int> cnt(mx + n, 0), left;
        for (int x : nums) cnt[x]++;
        int ans = 0;
        for (int x = 0; x < mx + n; x++) {
            if (cnt[x] >= 2) {
                left.insert(left.end(), cnt[x] - 1, x);
            } else if (!left.empty() && cnt[x] == 0) {
                ans += x - left.back();
                left.pop_back();
            }
        }
        return ans;
    }
    int solve2b(vector<int>& nums) {
        int n = nums.size(), mx = *max_element(nums.begin(), nums.end());
        vector<int> cnt(mx + n, 0);
        for (int x : nums) cnt[x]++;
        int ans = 0, left = 0;
        for (int x = 0; x < mx + n; x++) {
            if (cnt[x] >= 2) {
                left += cnt[x] - 1;
                ans -= x * (cnt[x] - 1);
            } else if (left > 0 && cnt[x] == 0) {
                ans += x;
                left--;
            }
        }
        return ans;
    }
};
// @lc code=end