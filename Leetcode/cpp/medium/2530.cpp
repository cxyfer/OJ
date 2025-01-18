/*
 * @lc app=leetcode.cn id=2530 lang=cpp
 *
 * [2530] 执行 K 次操作后的最大分数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<int> hp(nums.begin(), nums.end());
        long long ans = 0;
        for (int i = 0; i < k; i++) {
            int x = hp.top();
            hp.pop();
            ans += x;
            // hp.push(ceil(x / 3.0));
            hp.push((x + 2) / 3);
        }
        return ans;
    }
};
// @lc code=end

