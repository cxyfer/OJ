/*
 * @lc app=leetcode.cn id=2598 lang=cpp
 * @lcpr version=30204
 *
 * [2598] 执行操作后的最大 MEX
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution1 {
public:
    int findSmallestInteger(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> cnt(k);
        for (int x : nums) cnt[(x % k + k) % k]++;
        for (int mex = 0; mex <= n; mex++) {
            int r = mex % k;
            if (cnt[r] == 0) return mex;
            cnt[r]--;
        }
        return -1;
    }
};

class Solution2 {
public:
    int findSmallestInteger(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> cnt(k);
        for (int x : nums) cnt[(x % k + k) % k]++;
        int mn = ranges::min(cnt);
        return mn * k + ranges::distance(cnt.begin(), ranges::find(cnt, mn));
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [1,-10,7,13,6,8]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,-10,7,13,6,8]\n7\n
// @lcpr case=end

 */

