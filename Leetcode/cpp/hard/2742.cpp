/*
 * @lc app=leetcode.cn id=2742 lang=cpp
 *
 * [2742] 给墙壁刷油漆
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

class Solution1 {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        int n = cost.size();
        unordered_map<int, int> memo[n + 1]; // j can be negative, if use vector, need to shift
        function<int(int, int)> dfs = [&](int i, int j) {
            if (j >= i) return 0;
            if (i == 0) return INT_MAX / 2;  // avoid overflow
            if (memo[i].count(j)) return memo[i][j];
            return memo[i][j] = min(dfs(i - 1, j - 1),
                                    dfs(i - 1, j + time[i - 1]) + cost[i - 1]);
        };
        return dfs(n, 0);
    }
};

class Solution2a {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        int n = cost.size();
        vector<vector<int>> memo(n + 1, vector<int>(n + 1, -1));
        function<int(int, int)> dfs = [&](int i, int j) {
            if (j <= 0) return 0;
            if (i == 0) return INT_MAX / 2; // avoid overflow
            if (memo[i][j] != -1) return memo[i][j];
            return memo[i][j] = min(dfs(i - 1, j),
                                    dfs(i - 1, j - time[i - 1] - 1) + cost[i - 1]);
        };
        return dfs(n, n);
    }
};

class Solution2b {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        int n = cost.size();
        vector<int> dp(n + 1, INT_MAX / 2);
        dp[0] = 0;
        for (int i = 0; i < n; i++)
            for (int j = n; j > 0; j--)
                dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i]);
        return dp[n];
    }
};

// class Solution : public Solution1{};
class Solution : public Solution2a{};
// class Solution : public Solution2b{};
// @lc code=end
