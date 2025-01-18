/*
 * @lc app=leetcode.cn id=930 lang=cpp
 *
 * [930] 和相同的二元子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int ans = 0, s = 0;
        unordered_map<int, int> cnt;
        cnt[0] = 1;
        for (int i = 0; i < nums.size(); i++) {
            s += nums[i];
            ans += cnt[s - goal];
            cnt[s]++;
        }
        return ans;
    }
};
// @lc code=end

