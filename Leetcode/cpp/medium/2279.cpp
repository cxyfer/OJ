/*
 * @lc app=leetcode.cn id=2279 lang=cpp
 * @lcpr version=30204
 *
 * [2279] 装满石头的背包的最大数量
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        int n = capacity.size();
        vector<int> diffs(n);
        for (int i = 0; i < n; i++) diffs[i] = capacity[i] - rocks[i];
        sort(diffs.begin(), diffs.end());
        for (int i = 0; i < n; i++) {
            if (additionalRocks < diffs[i]) return i;
            additionalRocks -= diffs[i];
        }
        return n;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,3,4,5]\n[1,2,4,4]\n2\n
// @lcpr case=end

// @lcpr case=start
// [10,2,2]\n[2,2,0]\n100\n
// @lcpr case=end

 */

