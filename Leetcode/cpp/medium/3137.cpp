/*
 * @lc app=leetcode id=3137 lang=cpp
 * @lcpr version=30201
 *
 * [3137] Minimum Number of Operations to Make Word K-Periodic
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minimumOperationsToMakeKPeriodic(string word, int k) {
        int n = word.size(), mx = 0;
        unordered_map<string, int> cnt;
        for (int i = 0; i < n; i += k) {
            cnt[word.substr(i, k)]++;
            mx = max(mx, cnt[word.substr(i, k)]);
        }
        return n / k - mx;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "leetcodeleet"\n4\n
// @lcpr case=end

// @lcpr case=start
// "leetcoleet"\n2\n
// @lcpr case=end

 */

