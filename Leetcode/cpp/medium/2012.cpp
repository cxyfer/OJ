/*
 * @lc app=leetcode id=2012 lang=cpp
 *
 * [2012] Sum of Beauty in the Array
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int sumOfBeauties(vector<int>& nums) {
        int n = nums.size();
        vector<int> sufMin(n);
        sufMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--)
            sufMin[i] = min(sufMin[i + 1], nums[i]);
        int ans = 0, preMax = nums[0];
        for (int i = 1; i <= n - 2; i++) {
            int& x = nums[i];
            if (preMax < x && x < sufMin[i + 1])
                ans += 2;
            else if (nums[i - 1] < x && x < nums[i + 1])
                ans++;
            preMax = max(preMax, x);
        }
        return ans;
    }
};
// @lc code=end