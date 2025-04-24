/*
 * @lc app=leetcode.cn id=63 lang=cpp
 * @lcpr version=30204
 *
 * [63] 不同路径 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> memo(m, vector<int>(n, -1));
        auto dfs = [&](this auto&& dfs, int i, int j) -> int {
            if (i == m || j == n || obstacleGrid[i][j] == 1) return 0;
            if (i == m - 1 && j == n - 1) return 1;
            if (memo[i][j] != -1) return memo[i][j];
            return memo[i][j] = dfs(i + 1, j) + dfs(i, j + 1);
        };
        return dfs(0, 0);
    }
};

class Solution2a {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> memo(m, vector<int>(n, -1));
        function<int(int, int)> dfs = [&](int i, int j) -> int {
            if (i < 0 || j < 0 || obstacleGrid[i][j] == 1) return 0;
            if (i == 0 && j == 0) return 1;
            if (memo[i][j] != -1) return memo[i][j];
            return memo[i][j] = dfs(i - 1, j) + dfs(i, j - 1);
        };
        return dfs(m - 1, n - 1);
    }
};

class Solution2b {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> f(m + 1, vector<int>(n + 1, 0));
        f[1][1] = obstacleGrid[0][0] == 0 ? 1 : 0;
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (i == 1 && j == 1) continue; // base case
                f[i][j] = (obstacleGrid[i-1][j-1] == 1) ? 0 : f[i-1][j] + f[i][j-1];
            }
        }
        return f[m][n];
    }
};

class Solution2c {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<int> f(n + 1, 0), nf(n + 1, 0);
        f[1] = 1;
        for (int i = 1; i <= m; ++i) {
            fill(nf.begin(), nf.end(), 0);
            for (int j = 1; j <= n; ++j)
                nf[j] = (obstacleGrid[i-1][j-1] == 1) ? 0 : nf[j-1] + f[j];
            swap(f, nf);
        }
        return f[n];
    }
};

class Solution2d {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<int> f(n + 1, 0);
        f[1] = 1;
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j)
                f[j] = (obstacleGrid[i - 1][j - 1] == 1) ? 0 : f[j - 1] + f[j];
        return f[n];
    }
};

// using Solution = Solution1;
// using Solution = Solution2a;
// using Solution = Solution2b;
// using Solution = Solution2c;
using Solution = Solution2d;
// @lc code=end



/*
// @lcpr case=start
// [[0,0,0],[0,1,0],[0,0,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,1],[0,0]]\n
// @lcpr case=end

 */

