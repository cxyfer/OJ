/*
 * @lc app=leetcode.cn id=498 lang=cpp
 * @lcpr version=30204
 *
 * [498] 对角线遍历
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        int x = 0, y = 0;
        vector<int> ans;
        for (int _ = 0; _ < m * n; _++) {
            ans.push_back(mat[x][y]);
            if (((x + y) & 1) == 0) {
                if (y == n - 1) x++;
                else if (x == 0) y++;
                else x--, y++;
            } else {
                if (x == m - 1) y++;
                else if (y == 0) x++;
                else x++, y--;
            }
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<int> ans;
        for (int k = 0; k < m + n - 1; k++) {
            int min_j = max(k - m + 1, 0);
            int max_j = min(k, n - 1);
            if (k & 1)
                for (int j = max_j; j >= min_j; j--)
                    ans.push_back(mat[k - j][j]);
            else
                for (int j = min_j; j <= max_j; j++)
                    ans.push_back(mat[k - j][j]);
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [[1,2,3],[4,5,6],[7,8,9]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2],[3,4]]\n
// @lcpr case=end

 */

