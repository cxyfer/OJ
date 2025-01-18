/*
 * @lc app=leetcode id=1913 lang=cpp
 * @lcpr version=30111
 *
 * [1913] Maximum Product Difference Between Two Pairs
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int INF = 0x3f3f3f3f;

class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        LL max1 = -INF, max2 = -INF, min1 = INF, min2 = INF;
        for (auto x : nums) {
            if (x > max1) {
                max2 = max1;
                max1 = x;
            } else if (x > max2) {
                max2 = x;
            }
            if (x < min1) {
                min2 = min1;
                min1 = x;
            } else if (x < min2) {
                min2 = x;
            }
        }
        return max1 * max2 - min1 * min2;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [5,6,2,7,4]\n
// @lcpr case=end

// @lcpr case=start
// [4,2,5,9,7,4,8]\n
// @lcpr case=end

 */

