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
/*
    1. Hash Table
    2. Bit Manipulation
        - 260. Single Number III
    3. Math
*/
// @lc code=start
using LL = long long;

class Solution1 {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> cnt(n * n + 1);
        for (auto& row : grid) for (auto& x : row) cnt[x]++;
        vector<int> ans(2);
        for (int i=1; i<=n*n; i++){
            if (cnt[i] == 2) ans[0] = i; // repeated, a
            else if (cnt[i] == 0) ans[1] = i; // missing, b
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        // xor all numbers
        int s = 0; // xor of all numbers
        for (auto& row : grid) for (auto& x : row) s ^= x;
        for (int i = 1; i <= n * n; i++) s ^= i;
        // group xor
        int lb = s & -s; // lowest bit of 1
        vector<int> ans(2);
        for (auto& row : grid) for (auto& x : row)
            ans[(x & lb) == 0] ^= x;
        for (int i = 1; i <= n * n; i++) ans[(i & lb) == 0] ^= i;
        // check if ans[0] is in grid
        for (auto& row : grid)
            if (find(row.begin(), row.end(), ans[0]) != row.end())
                return ans;
        return {ans[1], ans[0]};
    }
};

class Solution3 {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        LL m = n * n, d1 = 0, d2 = 0;
        for (auto& row : grid) for (auto& x : row){
            d1 += x; // sum of all numbers
            d2 += x * x; // sum of all squares
        }
        d1 -= m * (m + 1) / 2; // a - b
        d2 -= m * (m + 1) * (m * 2 + 1) / 6; // a^2 - b^2 = (a + b)(a - b)
        return {(int) (d2 / d1 + d1) / 2, (int) (d2 / d1 - d1) / 2}; // (a, b)
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// @lc code=end

/*
// @lcpr case=start
// [[1,3],[2,2]]\n
// @lcpr case=end

// @lcpr case=start
// [[9,1,7],[8,9,2],[3,4,6]]\n
// @lcpr case=end

 */

