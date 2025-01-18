/*
 * @lc app=leetcode id=1310 lang=cpp
 * @lcpr version=30122
 *
 * [1310] XOR Queries of a Subarray
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        XOR Prefix Sum
    */
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size(), m = queries.size();
        vector<int> xors(n + 1, 0); // xors[i] = arr[0] ^ arr[1] ^ ... ^ arr[i - 1]
        for (int i = 1; i <= n; i++) {
            xors[i] = xors[i - 1] ^ arr[i - 1];
        }
        vector<int> ans(m, 0);
        for (int i = 0; i < m; i++) {
            int l = queries[i][0], r = queries[i][1];
            ans[i] = xors[r + 1] ^ xors[l];
        }
        return ans;
    }
};
// @lc code=end


/*
// @lcpr case=start
// [1,3,4,8]\n[[0,1],[1,2],[0,3],[3,3]]\n
// @lcpr case=end

// @lcpr case=start
// [4,8,2,10]\n[[2,3],[1,3],[0,0],[0,3]]\n
// @lcpr case=end

 */

