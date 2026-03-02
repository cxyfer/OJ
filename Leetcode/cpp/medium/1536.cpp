/*
 * @lc app=leetcode id=1536 lang=cpp
 *
 * [1536] Minimum Swaps to Arrange a Binary Grid
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> tail0(n, n);
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 1) {
                    tail0[i] = n - j - 1;
                    break;
                }
            }
        }

        // Bubble Sort
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int tgt = n - i - 1;
            bool ok = false;
            for (int j = i; j < n; j++) {
                if (tail0[j] >= tgt) {
                    ok = true;
                    ans += j - i;
                    tail0.erase(tail0.begin() + j);
                    tail0.insert(tail0.begin() + i, tgt);
                    break;
                }
            }
            if (!ok) return -1;
        }
        return ans;
    }
};
// @lc code=end

