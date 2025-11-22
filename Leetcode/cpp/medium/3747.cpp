/*
 * @lc app=leetcode.cn id=3747 lang=cpp
 * @lcpr version=30204
 *
 * [3747] 统计移除零后不同整数的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long countDistinct(long long n) {
        string s = to_string(n);
        int m = s.size();

        // 9 + 9^2 + ... + 9^(m-1) = (9^m - 9) / 8
        long long pow9 = pow(9LL, m);
        long long ans = (pow9 - 9) / 8;

        for (int i = 0; i < m; ++i) {
            int d = s[i] - '0';
            if (d == 0) break;
            pow9 /= 9;
            ans += (d - 1) * pow9;
            if (i == m - 1) ans++;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 10\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

 */

