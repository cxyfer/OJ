/*
 * @lc app=leetcode.cn id=2561 lang=cpp
 * @lcpr version=30204
 *
 * [2561] 重排水果
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        unordered_map<int, int> cnt;
        for (auto [x, y] : views::zip(basket1, basket2)) cnt[x]++, cnt[y]--;
        int mn = ranges::min(views::keys(cnt));
        vector<int> A, B;
        for (auto [k, v] : cnt) {
            if (v & 1) return -1;
            ranges::copy(views::repeat(k, v >> 1), back_inserter(A));
            ranges::copy(views::repeat(k, -v >> 1), back_inserter(B));
        }
        ranges::sort(A);
        ranges::sort(B, greater<>());
        return ranges::fold_left(views::zip(A, B), 0LL, [&](long long acc, const auto& p) {
            auto [a, b] = p;
            return acc + min({a, b, mn * 2});
        });
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,2,2,2]\n[1,4,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [2,3,4,1]\n[3,2,5,1]\n
// @lcpr case=end

 */

