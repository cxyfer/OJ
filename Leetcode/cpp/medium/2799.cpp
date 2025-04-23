/*
 * @lc app=leetcode.cn id=2799 lang=cpp
 *
 * [2799] 统计完全子数组的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int n = nums.size();
        int need = unordered_set(nums.begin(), nums.end()).size();
        int ans = 0, left = 0;
        unordered_map<int, int> cnt;
        for (int right = 0; right < n; right++) {
            cnt[nums[right]]++;
            if (cnt[nums[right]] == 1) need--;
            while (need == 0)
                if (--cnt[nums[left++]] == 0) need++;
            ans += left;
        }
        return ans;
    }
};
// @lc code=end

