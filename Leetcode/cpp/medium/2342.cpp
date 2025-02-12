/*
 * @lc app=leetcode.cn id=2342 lang=cpp
 *
 * [2342] 数位和相等数对的最大和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
private:
    int digit_sum(int x) {
        int res = 0;
        while (x) {
            res += x % 10;
            x /= 10;
        }
        return res;
    }
public:
    int maximumSum(vector<int>& nums) {
        unordered_map<int, int> mp;
        int ans = -1;
        for (int x : nums) {
            int d = digit_sum(x);
            if (mp.count(d)) {
                ans = max(ans, x + mp[d]);
                mp[d] = max(mp[d], x);
            } else {
                mp[d] = x;
            }
        }
        return ans;
    }
};
// @lc code=end

