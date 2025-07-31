/*
 * @lc app=leetcode.cn id=2044 lang=cpp
 *
 * [2044] 统计按位或能得到最大值的子集数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution1 {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int mx = ranges::fold_left(nums, 0, bit_or{});
        int ans = 0;
        for (int s = 1; s < (1 << n); ++s) {
            int cur = 0;
            for (int i = 0; i < n; ++i)
                if (s & (1 << i)) cur |= nums[i];
            ans += (cur == mx);
        }
        return ans;
    }
};

class Solution2 {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int ans = 0, mx = 0;
        auto dfs = [&](this auto&& dfs, int i, int cur) -> void {
            if (i == n) {
                if (cur > mx) {
                    mx = cur;
                    ans = 1;
                } else if (cur == mx)
                    ans++;
                return;
            }
            dfs(i + 1, cur | nums[i]);
            dfs(i + 1, cur);
        };
        dfs(0, 0);
        return ans;
    }
};

class Solution3 {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int mx = ranges::fold_left(nums, 0, bit_or{});
        vector<unordered_map<int, int>> memo(n);
        auto dfs = [&](this auto&& dfs, int i, int cur) -> int {
            if (i == n) return cur == mx;
            if (memo[i].count(cur)) return memo[i][cur];
            return memo[i][cur] = dfs(i + 1, cur) + dfs(i + 1, cur | nums[i]);
        };
        return dfs(0, 0);
    }
};

class Solution4a {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int mx = ranges::fold_left(nums, 0, bit_or{});
        vector<int> f(1 << bit_width(static_cast<unsigned int>(mx)));
        f[0] = 1;
        for (int x : nums)
            for (int i = mx; i >= 0; --i) f[i | x] += f[i];
        return f[mx];
    }
};

class Solution4b {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int mx = ranges::fold_left(nums, 0, bit_or{});
        unordered_map<int, int> f, nf;
        f[0] = 1;
        for (int x : nums) {
            nf.clear();
            for (auto [y, cnt] : f) {
                nf[y] += cnt;
                nf[y | x] += cnt;
            }
            swap(f, nf);
        }
        return f[mx];
    }
};

// using Solution = Solution1;
// using Solution = Solution2;
// using Solution = Solution3;
// using Solution = Solution4a;
using Solution = Solution4b;
// @lc code=end

