/*
 * @lc app=leetcode.cn id=2483 lang=cpp
 * @lcpr version=30204
 *
 * [2483] 商店的最少代价
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int bestClosingTime(string customers) {
        int pre = 0, suf = ranges::count(customers, 'Y');
        int ans = 0, cost = suf;
        for (int i = 0; i < customers.size(); ++i) {
            if (customers[i] == 'N') pre++;
            else suf--;
            if (pre + suf < cost) {
                ans = i + 1;
                cost = pre + suf;
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "YYNY"\n
// @lcpr case=end

// @lcpr case=start
// "NNNNN"\n
// @lcpr case=end

// @lcpr case=start
// "YYYY"\n
// @lcpr case=end

 */

