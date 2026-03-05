/*
 * @lc app=leetcode id=1758 lang=cpp
 *
 * [1758] Minimum Changes To Make Alternating Binary String
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int minOperations(string s) {
        auto calc = [&](int b) -> int {
            int res = 0;
            for (auto [i, ch] : views::enumerate(s))
                res += (ch - '0') != ((i & 1) ^ b);
            return res;
        };
        return min(calc(0), calc(1));
    }
};
// @lc code=end

