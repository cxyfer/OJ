/*
 * @lc app=leetcode id=3192 lang=cpp
 *
 * [3192] Minimum Operations to Make Binary Array Elements Equal to One II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int ans = 0;
        for (int x : nums) {
            if (x == 0) ans += (1 - ans & 1); 
            else ans += (ans & 1);
        }
        return ans;
    }
};
// @lc code=end
