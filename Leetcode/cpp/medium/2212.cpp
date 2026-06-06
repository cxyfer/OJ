/*
 * @lc app=leetcode id=2212 lang=cpp
 *
 * [2212] Maximum Points in an Archery Competition
 */


// @lcpr-template-start
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> maximumBobPoints(int numArrows, vector<int>& aliceArrows) {
        int n = aliceArrows.size();

        vector<vector<int>> f(n + 1, vector<int>(numArrows + 1));
        for (const auto& [i, a] : views::enumerate(aliceArrows)) {
            int v = i, w = a + 1;
            for (int j = 0; j <= numArrows; ++j) {
                if (j >= w)
                    f[i + 1][j] = max(f[i][j], f[i][j - w] + v);
                else
                    f[i + 1][j] = f[i][j];
            }
        }

        int rem = numArrows;
        vector<int> ans(n);
        for (int i = n - 1; i >= 0; --i) {
            int v = i, w = aliceArrows[i] + 1;
            if (rem >= w && f[i + 1][rem] == f[i][rem - w] + v) {
                ans[i] = w;
                rem -= w;
            }
        }
        ans[0] += rem;
        return ans;
    }
};

class Solution2 {
public:
    vector<int> maximumBobPoints(int numArrows, vector<int>& aliceArrows) {
        int n = aliceArrows.size();

        vector<int> ans(n);
        int mx = 0;
        for (int msk = 0; msk < (1 << n); ++msk) {
            int cur = 0, rem = numArrows;
            for (const auto& [i, a] : views::enumerate(aliceArrows)) {
                if (msk >> i & 1) {
                    cur += i;
                    rem -= a + 1;
                }
            }
            if (rem >= 0 && cur > mx) {
                mx = cur;
                for (const auto& [i, a] : views::enumerate(aliceArrows)) {
                    if (msk >> i & 1)
                        ans[i] = a + 1;
                    else
                        ans[i] = 0;
                }
                ans[0] += rem;
            }
        }
        return ans;
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end

