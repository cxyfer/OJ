/*
 * @lc app=leetcode.cn id=649 lang=cpp
 * @lcpr version=30204
 *
 * [649] Dota2 参议院
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.size();
        queue<int> r, d;
        for (int i = 0; i < n; ++i) {
            if (senate[i] == 'R') r.push(i);
            else d.push(i);
        }
        while (!r.empty() && !d.empty()) {
            if (r.front() < d.front()) r.push(r.front() + n);
            else d.push(d.front() + n);
            r.pop();
            d.pop();
        }
        return d.empty() ? "Radiant" : "Dire";
    }
};
// @lc code=end



/*
// @lcpr case=start
// "RD"\n
// @lcpr case=end

// @lcpr case=start
// "RDD"\n
// @lcpr case=end

 */

