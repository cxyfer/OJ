/*
 * @lc app=leetcode.cn id=3274 lang=cpp
 *
 * [3274] 检查棋盘方格颜色是否相同
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool checkTwoChessboards(string coordinate1, string coordinate2) {
        int x1 = coordinate1[0] - 'a', y1 = coordinate1[1] - '0';
        int x2 = coordinate2[0] - 'a', y2 = coordinate2[1] - '0';
        return ((x1 + y1) & 1) == ((x2 + y2) & 1);
    }
};
// @lc code=end

