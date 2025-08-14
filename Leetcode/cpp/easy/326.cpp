/*
 * @lc app=leetcode id=326 lang=cpp
 * @lcpr version=30112
 *
 * [326] Power of Three
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MAX_N = 1 << 31 - 1;
int MAX_3 = 1;
auto init = []() {
    while (MAX_3 < MAX_N)
        MAX_3 *= 3;
    return 0;
}();

class Solution {
public:
    bool isPowerOfThree(int n) {
        return n > 0 && MAX_3 % n == 0;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 27\n
// @lcpr case=end

// @lcpr case=start
// 0\n
// @lcpr case=end

// @lcpr case=start
// -1\n
// @lcpr case=end

 */

