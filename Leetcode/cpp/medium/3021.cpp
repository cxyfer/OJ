/*
 * @lc app=leetcode.cn id=3021 lang=cpp
 * @lcpr version=30204
 *
 * [3021] Alice 和 Bob 玩鲜花游戏
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long flowerGame(int n, int m) {
        return ((n + 1LL) / 2) * (m / 2) + (n / 2) * ((m + 1LL) / 2);
    }
};
// @lc code=end



/*
// @lcpr case=start
// 3\n2\n
// @lcpr case=end

// @lcpr case=start
// 1\n1\n
// @lcpr case=end

 */

