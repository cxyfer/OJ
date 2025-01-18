/*
 * @lc app=leetcode.cn id=2225 lang=cpp
 *
 * [2225] 找出输掉零场或一场比赛的玩家
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        vector<vector<int>> ans(2);
        unordered_map<int, int> cnt; // 用 map 就不用排序，但會略慢一些
        for (auto& match : matches) {
            int x = match[0], y = match[1];
            if (!cnt.count(x)) cnt[x] = 0; // 插入 key
            cnt[y]++;
        }
        for (auto kv : cnt) {
            int k = kv.first, v = kv.second;
            if (cnt[k] == 0) ans[0].push_back(k);
            else if (cnt[k] == 1) ans[1].push_back(k);
        }
        sort(ans[0].begin(), ans[0].end());
        sort(ans[1].begin(), ans[1].end());
        return ans;
    }
};
// @lc code=end

