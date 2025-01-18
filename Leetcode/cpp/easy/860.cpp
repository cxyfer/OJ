/*
 * @lc app=leetcode id=860 lang=cpp
 * @lcpr version=30111
 *
 * [860] Lemonade Change
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int cnt5 = 0, cnt10 = 0;
        for (int x : bills) {
            if (x == 5) {
                cnt5++;
            } else if (x == 10) {
                cnt10++;
                cnt5--;
            } else {
                if (cnt10 > 0) {
                    cnt10--;
                    cnt5--;
                } else {
                    cnt5 -= 3;
                }
            }
            if (cnt5 < 0) {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end

/*
// @lcpr case=start
// [5,5,5,10,20]\n
// @lcpr case=end

// @lcpr case=start
// [5,5,10,10,20]\n
// @lcpr case=end

 */

