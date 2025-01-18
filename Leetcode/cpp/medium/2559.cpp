/*
 * @lc app=leetcode id=2559 lang=cpp
 * @lcpr version=30122
 *
 * [2559] Count Vowel Strings in Ranges
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        int n = words.size(), m = queries.size();
        vector<int> s(n+1, 0); // prefix sum
        for (int i=0; i<n; i++) {
            string w = words[i];
            s[i+1] = s[i] + (isvowel(w[0]) && isvowel(w.back()));
        }
        vector<int> ans(m, 0);
        for (int i=0; i<m; i++) {
            int l = queries[i][0], r = queries[i][1];
            ans[i] = s[r+1] - s[l];
        }
        return ans;
    }
    bool isvowel(char c) {
        return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["aba","bcb","ece","aa","e"]\n[[0,2],[1,4],[1,1]]\n
// @lcpr case=end

// @lcpr case=start
// ["a","e","i"]\n[[0,2],[0,1],[2,2]]\n
// @lcpr case=end

 */

