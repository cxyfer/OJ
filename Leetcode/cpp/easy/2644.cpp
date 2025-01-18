/*
 * @lc app=leetcode.cn id=2644 lang=cpp
 *
 * [2644] 找出可整除性得分最大的整数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        int mx = -1, ans = 0;
        for (int d : divisors) {
            int cur = 0;
            for (int x : nums) if (x % d ==0) cur++;
            if (cur > mx || cur == mx && d < ans) {
                mx = cur;
                ans = d;
            }
        }
        return ans;
    }
};
// @lc code=end

