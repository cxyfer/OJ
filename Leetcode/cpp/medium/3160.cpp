/*
 * @lc app=leetcode.cn id=3160 lang=cpp
 *
 * [3160] 所有球里面不同颜色的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        vector<int> ans;
        unordered_map<int, int> cnt, color;
        for (auto& q : queries) {
            int x = q[0], y = q[1];
            if (color.count(x)) {
                cnt[color[x]]--;
                if (cnt[color[x]] == 0) {
                    cnt.erase(color[x]);
                }
            }
            color[x] = y;
            cnt[color[x]]++;
            ans.push_back(cnt.size());
        }
        return ans;
    }
};
// @lc code=end