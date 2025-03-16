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

