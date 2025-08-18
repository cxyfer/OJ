/*
 * @lc app=leetcode.cn id=3648 lang=cpp
 * @lcpr version=30204
 *
 * [3648] 覆盖网格的最少传感器数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minSensors(int n, int m, int k) {
        int sz = 2 * k + 1;
        return ((n + sz - 1) / sz) * ((m + sz - 1) / sz);
    }
};
// @lc code=end



/*
// @lcpr case=start
// 5\n5\n1\n
// @lcpr case=end

// @lcpr case=start
// 2\n2\n2\n
// @lcpr case=end

 */

