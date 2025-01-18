/*
 * @lc app=leetcode id=2055 lang=cpp
 * @lcpr version=30122
 *
 * [2055] Plates Between Candles
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
        int n = s.size(), m = queries.size();
        vector<int> pre_sum(n+1, 0); // pre_sum[i+1] 表示前i個物品中的盤子數量
        vector<int> l(n, -1), r(n, -1); // l[i]/r[i] 表示第i個蠟燭 左邊/右邊 最近的盤子的位置 (包括自己)，若無則為-1
        for (int i = 0; i < n; i++) {
            int j = n-1-i;
            l[i] = s[i] == '|' ? i : (i > 0 ? l[i-1] : -1);
            r[j] = s[j] == '|' ? j : (j < n-1 ? r[j+1] : -1);
            pre_sum[i+1] = pre_sum[i] + (s[i] == '*');
        }
        int a, b, c, d;
        vector<int> ans(m, 0);
        for (int i = 0; i < m; i++) {
            a = queries[i][0], b = queries[i][1];
            c = r[a], d = l[b];
            if (c != -1 && c <= d) {
                ans[i] = pre_sum[d+1] - pre_sum[c];
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "**|**|***|"\n[[2,5],[5,9]]\n
// @lcpr case=end

// @lcpr case=start
// "***|**|*****|**||**|*"\n[[1,17],[4,5],[14,17],[5,11],[15,16]]\n
// @lcpr case=end

 */

