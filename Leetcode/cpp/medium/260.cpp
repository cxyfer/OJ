/*
 * @lc app=leetcode.cn id=260 lang=cpp
 *
 * [260] 只出现一次的数字 III
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        // return solve1(nums);
        return solve2(nums);
    }
    vector<int> solve1(vector<int>& nums) {
        unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        vector<int> ans;
        for (auto it = cnt.begin(); it != cnt.end(); it++) {
            if (it->second == 1) ans.push_back(it->first);
        }
        return ans;
    }
    vector<int> solve2(vector<int>& nums) {
        unsigned xor_sum = 0; // avoid overflow
        for (int x : nums) xor_sum ^= x;
        int lb = xor_sum & -xor_sum;
        vector<int> ans(2, 0);
        for (int x : nums) ans[(x & lb) == 0] ^= x;
        return ans;
    }
};
// @lc code=end

