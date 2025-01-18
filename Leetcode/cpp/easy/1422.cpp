/*
 * @lc app=leetcode id=1422 lang=cpp
 * @lcpr version=30112
 *
 * [1422] Maximum Score After Splitting a String
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxScore(string s) {
        int n = s.size();
        int ans = 0, cnt = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') cnt++;
        }
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == '0') cnt++;
            else cnt--;
            ans = max(ans, cnt);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "011101"\n
// @lcpr case=end

// @lcpr case=start
// "00111"\n
// @lcpr case=end

// @lcpr case=start
// "1111"\n
// @lcpr case=end

 */

