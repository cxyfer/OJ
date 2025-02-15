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
class Solution {
public:
    bool isPowerOfThree(int n) {
        while (n > 0 && n % 3 == 0){
            n /= 3;
        }
        return (n == 1);
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

