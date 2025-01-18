/*
 * @lc app=leetcode.cn id=1979 lang=cpp
 *
 * [1979] 找出数组的最大公约数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int gcd(int a, int b) {
        return b ? gcd(b, a % b) : a;
    }
    int findGCD(vector<int>& nums) {
        int mx, mn;
        mx = mn = nums[0];
        for (int x : nums) {
            mx = max(mx, x);
            mn = min(mn, x);
        }
        return gcd(mx, mn);
    }
};
// @lc code=end

