/*
 * @lc app=leetcode.cn id=3492 lang=cpp
 * @lcpr version=30204
 *
 * [3492] 船上可以装载的最大集装箱数量
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        return min(n * n, maxWeight / w);
    }
};
// @lc code=end



/*
// @lcpr case=start
// 2\n3\n15\n
// @lcpr case=end

// @lcpr case=start
// 3\n5\n20\n
// @lcpr case=end

 */

