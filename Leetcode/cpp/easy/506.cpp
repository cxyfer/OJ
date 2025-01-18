/*
 * @lc app=leetcode.cn id=506 lang=cpp
 *
 * [506] 相对名次
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        int n = score.size();
        vector<pair<int, int>> ranks;
        for (int i=0; i<n; i++){
            ranks.emplace_back(make_pair(score[i], i));
        }
        sort(ranks.begin(), ranks.end(), greater<pair<int, int>>());
        vector<string> ans(n);
        for (int rk=0; rk<n; rk++){
            int idx = ranks[rk].second;
            if (rk == 0) ans[idx] = "Gold Medal";
            else if (rk == 1) ans[idx] = "Silver Medal";
            else if (rk == 2) ans[idx] = "Bronze Medal";
            else ans[idx] = to_string(rk+1);
        }
        return ans;
    }
};
// @lc code=end

