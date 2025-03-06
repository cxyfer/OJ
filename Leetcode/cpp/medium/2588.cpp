/*
 * @lc app=leetcode id=2588 lang=cpp
 *
 * [2588] Count the Number of Beautiful Subarrays
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long beautifulSubarrays(vector<int>& nums) {
        long long ans = 0;
        int s = 0;
        unordered_map<int, int> mp;
        mp[0] = 1;
        for (int x : nums) {
            s ^= x;
            ans += mp[s]++;
        }
        return ans;
    }
};
// @lc code=end

