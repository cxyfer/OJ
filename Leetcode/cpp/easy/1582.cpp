/*
 * @lc app=leetcode id=1582 lang=cpp
 *
 * [1582] Special Positions in a Binary Matrix
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int n = mat[0].size();
        vector<int> cols(n);

        for (auto& row : mat)
            for (auto [j, x] : views::enumerate(row)) cols[j] += x;

        int ans = 0;
        for (auto& row : mat) {
            if (ranges::count(row, 1) != 1) continue;
            int j = ranges::find(row, 1) - row.begin();
            ans += (cols[j] == 1);
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<vector<int>> mat = {{1,0,0},{0,0,1},{1,0,0}};
    cout << sol.numSpecial(mat) << endl;
    return 0;
}