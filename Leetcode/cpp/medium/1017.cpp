/*
 * @lc app=leetcode id=1017 lang=cpp
 * @lcpr version=30122
 *
 * [1017] Convert to Base -2
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string baseNeg2(int n) {
        int q, r;
        string ans = "";
        while (n) {
            q = n / -2;
            r = n % -2;
            if (r < 0) {
                q += 1;
                r += 2;
            }
            ans += to_string(r);
            n = q;
        }
        reverse(ans.begin(), ans.end());
        return ans.empty() ? "0" : ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 4\n
// @lcpr case=end

 */

