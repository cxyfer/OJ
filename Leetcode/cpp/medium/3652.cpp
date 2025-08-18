/*
 * @lc app=leetcode.cn id=3652 lang=cpp
 * @lcpr version=30204
 *
 * [3652] 按策略买卖股票的最佳时机
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        int n = prices.size();
        vector<long long> sp(n + 1), ss(n + 1);
        for (int i = 0; i < n; ++i) {
            sp[i + 1] = sp[i] + prices[i];
            ss[i + 1] = ss[i] + strategy[i] * prices[i];
        }
        long long ans = ss[n];
        for (int i = k; i <= n; ++i) {
            long long origin = ss[n] - ss[i] + ss[i - k];
            long long sell = sp[i] - sp[i - k / 2];
            ans = max(ans, origin + sell);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,2,8]\n[-1,0,1]\n2\n
// @lcpr case=end

// @lcpr case=start
// [5,4,3]\n[1,1,0]\n2\n
// @lcpr case=end

 */

