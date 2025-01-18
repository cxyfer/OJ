/*
 * @lc app=leetcode id=3127 lang=cpp
 * @lcpr version=30122
 *
 * [3127] Make a Square with the Same Color
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool canMakeSquare(vector<vector<char>>& grid) {
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                unordered_map<char, int> cnt;
                for (int a = 0; a < 2; a++) {
                    for (int b = 0; b < 2; b++) {
                        cnt[grid[i+a][j+b]]++;
                    }
                }
                if (cnt['B'] >= 3 || cnt['W'] >= 3) {
                    return true;
                }
            }
        }
        return false;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [["B","W","B"],["B","W","W"],["B","W","B"]]\n
// @lcpr case=end

// @lcpr case=start
// [["B","W","B"],["W","B","W"],["B","W","B"]]\n
// @lcpr case=end

// @lcpr case=start
// [["B","W","B"],["B","W","W"],["B","W","W"]]\n
// @lcpr case=end

 */

