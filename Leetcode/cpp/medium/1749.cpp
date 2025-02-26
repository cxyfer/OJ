/*
 * @lc app=leetcode.cn id=1749 lang=cpp
 *
 * [1749] 任意子数组和的绝对值的最大值
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution1a {
   public:
    int maxAbsoluteSum(vector<int>& nums) {
        int n = nums.size(), res1 = 0, res2 = 0;
        vector<int> f1(n + 1, 0), f2(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            f1[i + 1] = max(f1[i] + x, x);
            f2[i + 1] = min(f2[i] + x, x);
            res1 = max(res1, f1[i + 1]);
            res2 = min(res2, f2[i + 1]);
        }
        return max(res1, -res2);
    }
};

class Solution1b {
   public:
    int maxAbsoluteSum(vector<int>& nums) {
        int f1 = 0, f2 = 0;
        int ans = INT_MIN / 2;
        for (auto const& x : nums) {
            f1 = max(f1 + x, x);
            f2 = min(f2 + x, x);
            ans = max(ans, max(f1, -f2));
        }
        return ans;
    }
};

class Solution2a {
   public:
    int maxAbsoluteSum(vector<int>& nums) {
        int ans = 0, s = 0, mx = 0, mn = 0;
        for (auto const& x : nums) {
            s += x;
            mx = max(mx, s);
            mn = min(mn, s);
            ans = max(ans, mx - mn);
        }
        return ans;
    }
};

class Solution2b {
   public:
    int maxAbsoluteSum(vector<int>& nums) {
        int s = 0, mx = 0, mn = 0;
        for (auto const& x : nums) {
            s += x;
            mx = max(mx, s);
            mn = min(mn, s);
        }
        return mx - mn;
    }
};

// class Solution : public Solution1a {};
// class Solution : public Solution1b {};
// class Solution : public Solution2a {};
class Solution : public Solution2b {};
// @lc code=end
