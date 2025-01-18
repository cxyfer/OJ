/*
 * @lc app=leetcode.cn id=2463 lang=cpp
 *
 * [2463] 最小移动总距离
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        int n = robot.size(), m = factory.size();
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end());

        // 令 dfs(i, j) 為前 i+1 個工廠修了 j+1 個機器人所需要的最小距離
        vector<vector<long long>> memo(m, vector<long long>(n, LLONG_MAX / 2));
        auto dfs = [&](auto&& dfs, int i, int j) -> long long {
            if (i < 0) return j < 0 ? 0 : LLONG_MAX / 2; // 如果還有機器人，則不合法
            if (j < 0) return 0; // 剪枝，沒有機器人了
            long long& res = memo[i][j];
            if (res != LLONG_MAX / 2) return res;
            res = dfs(dfs, i - 1, j); // factory[i] 修 0 個機器人
            long long dist = 0;
            int pos = factory[i][0], limit = factory[i][1];
            for (int k = 0; k < limit && k <= j; ++k) { // 枚舉 factory[i] 修 k + 1 個機器人
                dist += abs(robot[j - k] - pos);
                res = min(res, dist + dfs(dfs, i - 1, j - (k + 1)));
            }
            return res;
        };
        return dfs(dfs, m - 1, n - 1);
    }
};

class Solution2 {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        int n = robot.size(), m = factory.size();
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end());

        // 令 f[i][j] 為前 i 個工廠修了 j 個機器人所需要的最小距離
        vector<vector<long long>> f(m + 1, vector<long long>(n + 1, LLONG_MAX / 2));
        f[0][0] = 0;
        for (int i = 1; i <= m; ++i) {
            int pos = factory[i - 1][0], limit = factory[i - 1][1];
            for (int j = 0; j <= n; ++j) {
                f[i][j] = f[i - 1][j]; // factory[i] 修 0 個機器人
                long long dist = 0;
                for (int k = 1; k <= limit && k <= j; ++k) {
                    dist += abs(robot[j - k] - pos);
                    f[i][j] = min(f[i][j], dist + f[i - 1][j - k]);
                }
            }
        }
        return f[m][n];
    }
};

class Solution3 {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        int n = robot.size(), m = factory.size();
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end());

        // 令 f[i][j] 為前 i 個工廠修了 j 個機器人所需要的最小距離
        vector<long long> f(n + 1, LLONG_MAX / 2);
        f[0] = 0;
        for (int i = 0; i < m; ++i) {
            int pos = factory[i][0], limit = factory[i][1];
            vector<long long> new_f = f;
            for (int j = 0; j <= n; ++j) {
                new_f[j] = f[j]; // factory[i] 修 0 個機器人
                long long dist = 0;
                for (int k = 1; k <= limit && k <= j; ++k) {
                    dist += abs(robot[j - k] - pos);
                    new_f[j] = min(new_f[j], dist + f[j - k]);
                }
            }
            f = new_f;
        }
        return f[n];
    }
};

class Solution4 {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        int n = robot.size(), m = factory.size();
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end());

        // 令 f[i][j] 為前 i 個工廠修了 j 個機器人所需要的最小距離
        vector<long long> f(n + 1, LLONG_MAX / 2);
        f[0] = 0;
        for (int i = 0; i < m; ++i) {
            int pos = factory[i][0], limit = factory[i][1];
            for (int j = n; j >= 0; --j) {
                long long dist = 0;
                for (int k = 1; k <= limit && k <= j; ++k) {
                    dist += abs(robot[j - k] - pos);
                    f[j] = min(f[j], dist + f[j - k]);
                }
            }
        }
        return f[n];
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// class Solution : public Solution4 {};
// @lc code=end