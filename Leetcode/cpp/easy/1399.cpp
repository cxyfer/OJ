/*
 * @lc app=leetcode.cn id=1399 lang=cpp
 * @lcpr version=30204
 *
 * [1399] 统计最大组的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MAX_N = 1e4 + 5;

vector<int> ans(MAX_N, 0);
auto init = []() {
    auto digit = [](int x) {
        int res = 0;
        while (x) {
            res += x % 10;
            x /= 10;
        }
        return res;
    };

    int mx = 0;
    vector<int> cnt(9 * ceil(log10(MAX_N)) + 1, 0);
    for (int i = 1; i < MAX_N; i++) {
        int s = digit(i);
        cnt[s]++;
        if (cnt[s] > mx) {
            mx = cnt[s];
            ans[i] = 1;
        }
        else {
            ans[i] = ans[i - 1] + (cnt[s] == mx);
        }
    }
    return 0;
}();

class Solution1 {
public:
    int countLargestGroup(int n) {
        return ans[n];
    }
};

class Solution2 {
public:
    int countLargestGroup(int n) {
        vector<int> high;
        while (n) {
            high.push_back(n % 10);
            n /= 10;
        }
        reverse(high.begin(), high.end());
        int m = high.size();
        vector<vector<vector<int>>> memo(m, vector<vector<int>>(9 * m + 1, vector<int>(2, -1)));
        auto dfs = [&](this auto &&dfs, int i, int s, bool limit_high) -> int {
            if (i == m) return s == 0;
            if (s == 0) return 1;
            if (s < 0) return 0;
            if (memo[i][s][limit_high] != -1) return memo[i][s][limit_high];

            int hi = limit_high ? high[i] : 9;
            int res = 0;
            for (int d = 0; d <= hi; d++) {
                res += dfs(i + 1, s - d, limit_high && d == hi);
            }
            return memo[i][s][limit_high] = res;
        };
        int ans = 0, mx = 0;
        for (int tgt = 1; tgt <= 9 * m; tgt++) {
            int res = dfs(0, tgt, true);
            if (res > mx) mx = res, ans = 1;
            else if (res == mx) ans++;
        }
        return ans;
    }
};

using Solution = Solution2;
// @lc code=end

/*
// @lcpr case=start
// 13\n
// @lcpr case=end

// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 15\n
// @lcpr case=end

// @lcpr case=start
// 24\n
// @lcpr case=end

 */

