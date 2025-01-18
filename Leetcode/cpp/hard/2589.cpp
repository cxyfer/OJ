/*
 * @lc app=leetcode.cn id=2589 lang=cpp
 *
 * [2589] 完成所有任务的最少时间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        auto cmp = [](vector<int> &a, vector<int> &b) {
            return a[1] < b[1];
        };
        sort(tasks.begin(), tasks.end(), cmp);
        vector<bool> vis(tasks.back()[1] + 1, false);
        for (auto& t : tasks){
            int st = t[0], ed = t[1], d = t[2];
            d -= accumulate(vis.begin() + st, vis.begin() + ed + 1, 0);
            if (d <= 0) continue;
            int i = ed;
            for (int i = ed; i >= st && d; i--) {
                if (!vis[i]) {
                    vis[i] = true;
                    d--;
                }
            }
        }
        return accumulate(vis.begin(), vis.end(), 0);
    }
};
// @lc code=end

