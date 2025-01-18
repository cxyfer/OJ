/*
 * @lc app=leetcode id=2739 lang=cpp
 * @lcpr version=30122
 *
 * [2739] Total Distance Traveled
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int distanceTraveled(int mainTank, int additionalTank) {
        int q, r, ans = 0, used;
        while (mainTank >= 5) {
            q = mainTank / 5;
            r = mainTank % 5;
            ans += q * 5 * 10;
            used = min(q, additionalTank);
            mainTank = r + used;
            additionalTank -= used;
        }
        return ans + mainTank * 10;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 5\n10\n
// @lcpr case=end

// @lcpr case=start
// 1\n2\n
// @lcpr case=end

 */

