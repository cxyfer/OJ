/*
 * @lc app=leetcode id=1545 lang=cpp
 *
 * [1545] Find Kth Bit in Nth Binary String
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
vector<int> length(21, 0);
auto init = []() {
    for (int i = 1; i <= 20; i++) length[i] = length[i - 1] * 2 + 1;
    return 0;
}();

class Solution {
public:
    char findKthBit(int n, int k) {
        auto dfs = [&](this auto&& dfs, int n, int k) -> int {
            if (n == 1) return 0;
            int m = length[n - 1] + 1;
            if (k < m)
                return dfs(n - 1, k);
            else if (k == m)
                return 1;
            else
                return dfs(n - 1, m - (k - m)) ^ 1;
        };
        return '0' + dfs(n, k);
    }
};
// @lc code=end
