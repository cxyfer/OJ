/*
 * @lc app=leetcode.cn id=974 lang=cpp
 *
 * [974] 和可被 K 整除的子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int ans = 0, s = 0;
        vector<int> cnt(k);
        cnt[0] = 1;
        for (int x : nums) {
            s = (s + (x % k) + k) % k; // 避免出現負數
            ans += cnt[s];
            cnt[s]++;
        }
        return ans;
    }
};
// @lc code=end

