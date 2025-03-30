/*
 * @lc app=leetcode.cn id=2980 lang=cpp
 * @lcpr version=30204
 *
 * [2980] Check if Bitwise OR Has Trailing Zeros
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool hasTrailingZeros(vector<int>& nums) {
        int cnt = 0;
        for (int x : nums) cnt += x & 1 ^ 1;
        return cnt >= 2;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [2,4,8,16]\n
// @lcpr case=end

// @lcpr case=start
// [1,3,5,7,9]\n
// @lcpr case=end

 */

