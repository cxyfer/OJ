/*
 * @lc app=leetcode.cn id=1680 lang=cpp
 * @lcpr version=30204
 *
 * [1680] 连接连续二进制数字
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using i64 = long long;
using u32 = uint32_t;
const int MOD = 1e9 + 7;

class Solution {
public:
    int concatenatedBinary(int n) {
        i64 ans = 0;
        for (u32 i = 1; i <= n; i++) {
            ans = (ans << bit_width(i)) | i;
            ans %= MOD;
        }
        return static_cast<int>(ans);
    }
};
// @lc code=end



/*
// @lcpr case=start
// 1\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 12\n
// @lcpr case=end

 */

