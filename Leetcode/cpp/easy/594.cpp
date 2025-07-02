/*
 * @lc app=leetcode.cn id=594 lang=cpp
 * @lcpr version=30204
 *
 * [594] 最长和谐子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        int ans = 0;
        for (auto [k, v] : cnt)
            if (cnt.count(k + 1))
                ans = max(ans, v + cnt[k + 1]);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3,2,2,5,2,3,7]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1]\n
// @lcpr case=end

 */

