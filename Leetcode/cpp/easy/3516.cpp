/*
 * @lc app=leetcode.cn id=3516 lang=cpp
 * @lcpr version=30204
 *
 * [3516] 找到最近的人
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findClosest(int x, int y, int z) {
        int d1 = abs(x - z), d2 = abs(y - z);
        return d1 == d2 ? 0 : (d1 < d2 ? 1 : 2);
    }
};
// @lc code=end



/*
// @lcpr case=start
// 2\n7\n4\n
// @lcpr case=end

// @lcpr case=start
// 2\n5\n6\n
// @lcpr case=end

// @lcpr case=start
// 1\n5\n3\n
// @lcpr case=end

 */

