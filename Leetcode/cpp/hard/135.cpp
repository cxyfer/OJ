/*
 * @lc app=leetcode.cn id=135 lang=cpp
 * @lcpr version=30204
 *
 * [135] 分发糖果
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> suf(n, 1);
        for (int i = n - 2; i >= 0; i--)
            if (ratings[i] > ratings[i + 1])
                suf[i] = suf[i + 1] + 1;
        int ans = 0, pre = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0 && ratings[i] > ratings[i - 1])
                pre += 1;
            else
                pre = 1;
            ans += max(pre, suf[i]);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,0,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,2]\n
// @lcpr case=end

 */

