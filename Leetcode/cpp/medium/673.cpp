/*
 * @lc app=leetcode.cn id=673 lang=cpp
 * @lcpr version=30204
 *
 * [673] 最长递增子序列的个数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
# include <ranges>
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int mx = ranges::max(nums);
        auto vals = nums;
        ranges::sort(vals);
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        int sz = vals.size();
        unordered_map<int, int> mp;
        for (auto [i, v] : views::enumerate(vals)) mp[v] = i + 1;

        vector<pair<int, int>> tree(sz + 1);
        auto update = [&](int k, int mx, int cnt) {
            while (k < tree.size()) {
                // tree[k] += x
                if (mx > tree[k].first) tree[k] = {mx, cnt};
                else if (mx == tree[k].first) tree[k].second += cnt;
                k += (k & -k);
            }
        };

        auto query = [&](int k) {
            pair<int, int> res = {0, 0};
            while (k > 0) {
                // res += tree[k]
                if (tree[k].first > res.first) res = tree[k];
                else if (tree[k].first == res.first) res.second += tree[k].second;
                k -= (k & -k);
            }
            return res;
        };
        
        for (auto v : nums) {
            auto [mx, cnt] = query(mp[v] - 1);
            update(mp[v], mx + 1, max(cnt, 1));
        }
        return query(sz).second;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3,5,4,7]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2,2,2]\n
// @lcpr case=end

 */

