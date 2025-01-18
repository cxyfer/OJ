/*
 * @lc app=leetcode id=2413 lang=cpp
 * @lcpr version=30111
 *
 * [2413] Smallest Even Multiple
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int smallestEvenMultiple(int n) {
        return (n & 1) ? n << 1 : n;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 5\n
// @lcpr case=end

// @lcpr case=start
// 6\n
// @lcpr case=end

 */

