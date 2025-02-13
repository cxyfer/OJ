/*
 * @lc app=leetcode.cn id=3066 lang=cpp
 *
 * [3066] 超过阈值的最少操作数 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int ans = 0;
        priority_queue<int, vector<int>, greater<int>> hp(nums.begin(), nums.end());
        while (hp.top() < k) {
            int x = hp.top(); hp.pop();
            int y = hp.top(); hp.pop();
            hp.push(x * 2 + y);
            ans++;
        }
        return ans;
    }
};
// @lc code=end