/*
 * @lc app=leetcode id=2965 lang=cpp
 * @lcpr version=30112
 *
 * [2965] Find Missing and Repeated Values
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    /*
        1. Hash Table
        2. Bit Manipulation
            - 260. Single Number III
        3. Math
    */
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        // return solve1(grid);
        // return solve2(grid);
        return solve3(grid);
    }
    vector<int> solve1(vector<vector<int>>& grid) {
        int n = grid.size();
        unordered_map<int, int> cnt;
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
                cnt[grid[i][j]]++;
        vector<int> ans(2);
        for (int i=1; i<=n*n; i++){
            if (cnt[i] == 2) ans[0] = i; // repeated, a
            else if (cnt[i] == 0) ans[1] = i; // missing, b
        }
        return ans;
    }
    vector<int> solve2(vector<vector<int>>& grid) {
        int n = grid.size();
        // xor all numbers
        int s = 0; // xor of all numbers
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
                s ^= grid[i][j];
        for (int i=1; i<=n*n; i++)
            s ^= i;
        // group xor
        int lb = s & -s; // lowest bit of 1
        vector<int> ans(2);
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
                ans[(grid[i][j] & lb) == 0] ^= grid[i][j];
        for (int i=1; i<=n*n; i++)
            ans[(i & lb) == 0] ^= i;
        // check if ans[0] is in grid
        for (auto& row : grid)
            if (find(row.begin(), row.end(), ans[0]) != row.end())
                return ans;
        return {ans[1], ans[0]};
    }
    vector<int> solve3(vector<vector<int>>& grid) {
        int n = grid.size();
        LL m = n * n, d1 = 0, d2 = 0;
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++){
                d1 += grid[i][j]; // sum of all numbers
                d2 += grid[i][j] * grid[i][j]; // sum of all squares
            }
        d1 -= m * (m + 1) / 2; // a - b
        d2 -= m * (m + 1) * (m * 2 + 1) / 6; // a^2 - b^2 = (a + b)(a - b)
        return {(int) (d2 / d1 + d1) / 2, (int) (d2 / d1 - d1) / 2}; // (a, b)
    }
};
// @lc code=end

/*
// @lcpr case=start
// [[1,3],[2,2]]\n
// @lcpr case=end

// @lcpr case=start
// [[9,1,7],[8,9,2],[3,4,6]]\n
// @lcpr case=end

 */

