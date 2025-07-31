/*
 * @lc app=leetcode.cn id=3370 lang=cpp
 * @lcpr version=30204
 *
 * [3370] 仅含置位位的最小整数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int smallestNumber(int n) {
        return (1 << bit_width(static_cast<uint32_t>(n))) - 1;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 5\n
// @lcpr case=end

// @lcpr case=start
// 10\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

 */

