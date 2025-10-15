/*
 * @lc app=leetcode.cn id=3712 lang=cpp
 * @lcpr version=30204
 *
 * [3712] 出现次数能被 K 整除的元素总和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int sumDivisibleByK(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        for (auto x : nums) cnt[x]++;
        int ans = 0;
        for (auto [x, v] : cnt)
            if (v % k == 0)
                ans += x * v;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,2,3,3,3,3,4]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5]\n2\n
// @lcpr case=end

// @lcpr case=start
// [4,4,4,1,2,3]\n3\n
// @lcpr case=end

 */

