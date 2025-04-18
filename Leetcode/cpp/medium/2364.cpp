/*
 * @lc app=leetcode.cn id=2364 lang=cpp
 * @lcpr version=30204
 *
 * [2364] 统计坏数对的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        int n = nums.size();
        long long ans = (long long)n * (n - 1) / 2;
        unordered_map<int, int> cnt;
        for (int j = 0; j < n; j++) ans -= cnt[j - nums[j]]++;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,1,3,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

 */

