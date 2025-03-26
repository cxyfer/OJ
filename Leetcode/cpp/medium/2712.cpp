/*
 * @lc app=leetcode.cn id=2712 lang=cpp
 * @lcpr version=30204
 *
 * [2712] 使所有字符相等的最小成本
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;

class Solution1 {
public:
    LL minimumCost(string s) {
        int n = s.size();
        LL ans = 0;
        for (int i = 0; i < n - 1; i++)
            if (s[i] != s[i + 1])
                ans += min(i + 1, n - i - 1);
        return ans;
    }
};

class Solution2a {
public:
    LL minimumCost(string s) {
        int n = s.size();
        // pre(i, j) 表示只透過操作1，將 s[:i+1] 變成 j 的最小成本
        vector<vector<LL>> memo1(n, vector<LL>(2, -1));
        auto pre = [&](this auto&& pre, int i, int j) -> LL {
            if (i == -1) return 0;
            LL& res = memo1[i][j];
            if (res != -1) return res;
            return res = pre(i - 1, s[i] - '0') + (s[i] != '0' + j) * (i + 1);
        };
        // suf(i, j) 表示只透過操作2，將 s[i:] 變成 j 的最小成本
        vector<vector<LL>> memo2(n, vector<LL>(2, -1));
        auto suf = [&](this auto&& suf, int i, int j) -> LL {
            if (i == n) return 0;
            LL& res = memo2[i][j];
            if (res != -1) return res;
            return res = suf(i + 1, s[i] - '0') + (s[i] != '0' + j) * (n - i);
        };
        LL ans = LLONG_MAX;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < 2; j++)
                ans = min(ans, pre(i, j) + suf(i + 1, j));
        return ans;
    }
};

class Solution2b {
public:
    LL minimumCost(string s) {
        int n = s.size();
        // suf[i][j] 表示只透過操作2，將 s[i:] 變成 j 的最小成本
        vector<vector<LL>> suf(n + 1, vector<LL>(2, 0));
        for (int i = n - 1; i >= 0; i--) {
            int x = s[i] - '0';
            for (int j = 0; j < 2; j++)
                suf[i][j] = suf[i + 1][x] + (x != j) * (n - i);
        }
        vector<LL> pre(2, 0);
        LL ans = LLONG_MAX;
        for (int i = 0; i < n; i++) {
            int x = s[i] - '0';
            for (int j = 0; j < 2; j++) {
                pre[j] = pre[x] + (x != j) * (i + 1);
                ans = min(ans, pre[j] + suf[i + 1][j]);
            }
        }
        return ans;
    }
};

using Solution = Solution1;
// using Solution = Solution2a;
// using Solution = Solution2b;
// @lc code=end

/*
// @lcpr case=start
// "0011"\n
// @lcpr case=end

// @lcpr case=start
// "010101"\n
// @lcpr case=end

 */

