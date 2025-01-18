/*
 * @lc app=leetcode id=1177 lang=cpp
 * @lcpr version=30122
 *
 * [1177] Can Make Palindrome from Substring
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        int n = s.size(), m = queries.size();
        vector<int> xors(n+1, 0);
        for (int i = 0; i < n; i++) {
            xors[i+1] = xors[i] ^ (1 << (s[i] - 'a'));
        }
        vector<bool> ans(m, false);
        for (int i = 0; i < m; i++) {
            int l = queries[i][0], r = queries[i][1], k = queries[i][2];
            int cnt = bit_count(xors[r+1] ^ xors[l]);
            ans[i] = cnt / 2 <= k;
        }
        return ans;
    }
    int bit_count(int x) {
        int cnt = 0;
        while (x) {
            x &= (x - 1); // clear the least significant bit
            cnt++;
        }
        return cnt;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abcda"\n[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]\n
// @lcpr case=end

// @lcpr case=start
// "lyb"\n[[0,1,0],[2,2,1]]\n
// @lcpr case=end

 */

