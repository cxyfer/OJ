/*
 * @lc app=leetcode.cn id=2272 lang=cpp
 * @lcpr version=30204
 *
 * [2272] Substring With Largest Variance
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
假設已知在答案中出現次數最多和最少的字母分別為 a 和 b，
則可以將 a 視為 1，b 視為 -1，其他字母視為 0，
如此題目所求即為對其求 Maximum Subarray Sum。

但不同的是 b 一定要出現，也就是不能只有 a 出現，因此需要額外維護一個狀態紀錄 b 是否出現過。
- 令 f[i][0] 為以 i 為結尾的子陣列中，a 出現次數減去 b 出現次數的最大值。
- 令 f[i][1] 為以 i 為結尾的子陣列中，a 出現次數減去 b 出現次數的最大值，且 b 至少出現過一次。

但 (a, b) 其實是未知的，不過所有可能只有 P(26, 2) = 650 種，可以枚舉。
若枚舉的 a' 並不是真正的 a，或若枚舉的 b' 並不是真正的 b，則最大子陣列和都會變小，不影響答案。
*/
// @lc code=start
class Solution {
public:
    int largestVariance(string s) {
        int ans = 0;
        for (char a = 'a'; a <= 'z'; a++) {
            for (char b = 'a'; b <= 'z'; b++) {
                if (a == b) continue;
                int f0 = 0, f1 = INT_MIN / 2;
                for (char& ch : s) {
                    if (ch == a) {
                        f0 = max(f0, 0) + 1;
                        f1++;
                    } else if (ch == b) {
                        int t = f0;
                        f0 = max(f0, 0) - 1;
                        f1 = max({t, f1, 0}) - 1;
                    }
                    ans = max(ans, f1);
                }
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "aababbb"\n
// @lcpr case=end

// @lcpr case=start
// "abcde"\n
// @lcpr case=end

 */

