/*
 * @lc app=leetcode.cn id=179 lang=cpp
 * @lcpr version=30204
 *
 * [179] 最大数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        auto cmp = [](const string& a, const string& b) -> bool {
            return a + b > b + a;
        };
        auto s = nums | views::transform([](int x) { return to_string(x); }) |
                 ranges::to<vector<string>>();
        ranges::sort(s, cmp);
        return (s[0] == "0")
                   ? "0"
                   : ranges::fold_left(s, "", [](string a, const string& b) {
            return a + b;
        });
    }
};
// @lc code=end



/*
// @lcpr case=start
// [10,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,30,34,5,9]\n
// @lcpr case=end

 */

