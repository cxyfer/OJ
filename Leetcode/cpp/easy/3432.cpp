/*
 * @lc app=leetcode.cn id=3432 lang=cpp
 *
 * [3432] 统计元素和差值为偶数的分区方案
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countPartitions(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        vector<int> s(n + 1);
        for (int i = 0; i < n; ++i) {
            s[i + 1] = s[i] + nums[i];
        }
        for (int i = 0; i < n - 1; ++i) {
            if (abs(s[i] - (s[n] - s[i])) % 2 == 0) {
                ans += 1;
            }
        }
        return ans;
    }
};
// @lc code=end