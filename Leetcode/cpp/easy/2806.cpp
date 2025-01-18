/*
 * @lc app=leetcode.cn id=2806 lang=cpp
 *
 * [2806] 取整购买后的账户余额
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int accountBalanceAfterPurchase(int purchaseAmount) {
        return solve1(purchaseAmount);
        // return solve2(purchaseAmount);
    }
    int solve1(int purchaseAmount) {
        int x = purchaseAmount / 10;
        int cost1 = x * 10, cost2 = (x + 1) * 10;
        if (purchaseAmount - cost1 < cost2 - purchaseAmount)
            return 100 - cost1;
        else
            return 100 - cost2;
    }
    int solve2(int purchaseAmount) {
        return 100 - (purchaseAmount + 5) / 10 * 10;
    }
};
// @lc code=end