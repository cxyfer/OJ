/*
 * @lc app=leetcode id=2579 lang=cpp
 *
 * [2579] Count Total Number of Colored Cells
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
/*
  2 * (1 + 3 + ... + (2n - 1)) - (2n - 1)
= 2 * ((1 + (2n - 1)) * n / 2) - (2n - 1)
= 2 * (n^2) - (2n - 1)
= 2n^2 - 2n + 1
*/
class Solution {
public:
    long long coloredCells(int n) {
        return 2LL * n * n - 2LL * n + 1LL;
    }
};
// @lc code=end

