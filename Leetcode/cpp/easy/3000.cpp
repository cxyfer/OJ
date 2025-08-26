/*
 * @lc app=leetcode.cn id=3000 lang=cpp
 * @lcpr version=30204
 *
 * [3000] 对角线最长的矩形的面积
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        // return max((x * x + y * y, x * y) for x, y in dimensions)[1]
        return ranges::max(dimensions | views::transform([](const auto& d) {
            return make_pair(d[0] * d[0] + d[1] * d[1], d[0] * d[1]);
        })).second;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<vector<int>> dimensions;
    dimensions = {{9, 3}, {8, 6}};
    cout << sol.areaOfMaxDiagonal(dimensions) << endl;
    dimensions = {{3, 4}, {4, 3}};
    cout << sol.areaOfMaxDiagonal(dimensions) << endl;
    return 0;
}

/*
// @lcpr case=start
// [[9,3],[8,6]]\n
// @lcpr case=end

// @lcpr case=start
// [[3,4],[4,3]]\n
// @lcpr case=end

 */

