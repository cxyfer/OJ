/*
 * @lc app=leetcode.cn id=560 lang=cpp
 *
 * [560] 和为 K 的子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int ans = 0, s = 0;
        unordered_map<int, int> cnt;
        cnt[0] = 1;
        for (int i = 0; i < nums.size(); i++) {
            s += nums[i];
            ans += cnt[s - k];
            cnt[s]++;
        }
        return ans;
    }
};
// @lc code=end

