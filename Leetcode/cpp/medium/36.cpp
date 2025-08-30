/*
 * @lc app=leetcode.cn id=36 lang=cpp
 * @lcpr version=30204
 *
 * [36] 有效的数独
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> row(9), col(9), box(9);
        for (auto [i, line] : views::enumerate(board)) {
            for (auto [j, ch] : views::enumerate(line)) {
                if (ch == '.') continue;
                int msk = 1 << (ch - '1');
                if (row[i] & msk || col[j] & msk || box[i / 3 * 3 + j / 3] & msk) return false;
                row[i] |= msk;
                col[j] |= msk;
                box[i / 3 * 3 + j / 3] |= msk;
            }
        }
        return true;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
// @lcpr case=end

// @lcpr case=start
// [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
// @lcpr case=end

 */

