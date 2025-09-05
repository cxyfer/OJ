/*
 * @lc app=leetcode.cn id=2749 lang=cpp
 * @lcpr version=30204
 *
 * [2749] 得到整数零需要执行的最少操作数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using ll = long long;
class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        for (ll k = 1; k <= 32; k++) {
            ll x = num1 - k * num2;
            if (__builtin_popcountll(x) <= k && k <= x)
                return k;
        }
        return -1;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 3\n-2\n
// @lcpr case=end

// @lcpr case=start
// 5\n7\n
// @lcpr case=end

 */

