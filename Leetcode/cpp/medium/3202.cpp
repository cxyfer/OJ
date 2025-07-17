/*
 * @lc app=leetcode.cn id=3202 lang=cpp
 * @lcpr version=30204
 *
 * [3202] 找出有效子序列的最大长度 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution1 {
public:
    int maximumLength(vector<int>& nums, int k) {
        auto arr = nums | views::transform([k](int x) { return x % k; });
        int ans = 0;
        for (int s = 0; s < k; ++s) {
            vector<int> f(k, 0);
            for (int x : arr)
                f[x] = f[(s - x + k) % k] + 1;
            ans = max(ans, ranges::max(f));
        }
        return ans;
    }
};

class Solution2 {
public:
    int maximumLength(vector<int>& nums, int k) {
        vector<vector<int>> f(k, vector<int>(k, 0));
        for (int x : nums | views::transform([k](int x) { return x % k; }))
            for (int y = 0; y < k; ++y)
                f[y][x] = f[x][y] + 1;
        return ranges::max(f | views::transform(ranges::max));
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,4,2,3,1,4]\n3\n
// @lcpr case=end

 */

