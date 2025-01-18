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
class Solution1 {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int mx = 0;
        for (int x : nums) mx |= x;
        int ans = 0;
        for (int s = 1; s < (1 << n); ++s) {
            int cur = 0;
            for (int i = 0; i < n; ++i) {
                if (s & (1 << i)) cur |= nums[i];
            }
            if (cur == mx) ans++;
        }
        return ans;
    }
};

class Solution2 {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int mx = 0;
        for (int x : nums) mx |= x;
        int ans = 0;
        for (int s = 1; s < (1 << n); ++s) {
            int cur = 0;
            for (int i = 0; i < n; ++i) {
                if (s & (1 << i)) cur |= nums[i];
            }
            if (cur == mx) ans++;
        }
        return ans;
    }
};
// class Solution2:
//     def countMaxOrSubsets(self, nums: List[int]) -> int:
//         ans = mx = 0
//         def dfs(i, cur):
//             nonlocal ans, mx
//             if i == len(nums):
//                 if cur == mx:
//                     ans += 1
//                 elif cur > mx:
//                     mx = cur
//                     ans = 1
//                 return
//             dfs(i + 1, cur | nums[i])
//             dfs(i + 1, cur)
//         dfs(0, 0)
//         return ans
class Solution4 {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int mx = 0;
        for (int x : nums) mx |= x; 
        vector<unordered_map<int, int>> memo(n);
        auto dfs = [&](auto&& self, int i, int cur) -> int {
            if (i == n) return cur == mx;
            if (memo[i].count(cur)) return memo[i][cur];
            return memo[i][cur] = self(self, i + 1, cur) + self(self, i + 1, cur | nums[i]);
        };
        return dfs(dfs, 0, 0);
    }
};
// class Solution : public Solution1 {};
class Solution : public Solution4 {};
// @lc code=end

