/*
 * @lc app=leetcode.cn id=826 lang=cpp
 *
 * [826] 安排工作以达到最大收益
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        // return solve1(difficulty, profit, worker);
        return solve2(difficulty, profit, worker);
    }
    int solve1(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int n = difficulty.size(), m = worker.size();
        vector<pair<int, int>> tasks;
        for (int i = 0; i < n; i++) tasks.push_back({difficulty[i], profit[i]});
        sort(tasks.begin(), tasks.end());
        sort(worker.begin(), worker.end());
        int ans = 0, i = 0, mx = 0;
        for (int w : worker) {
            while (i < n && tasks[i].first <= w) { // find the last task that can be done
                mx = max(mx, tasks[i].second); // max profit
                i++;
            }
            ans += mx;
        }
        return ans;
    }
    int solve2(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int n = difficulty.size(), m = worker.size();
        vector<pair<int, int>> tasks;
        for (int i = 0; i < n; i++) tasks.push_back({difficulty[i], profit[i]});
        sort(tasks.begin(), tasks.end()); // sort by difficulty
        vector<int> max_profit(n, 0); // max_profit[i] = max profit of tasks[0:i+1]
        max_profit[0] = tasks[0].second;
        for (int i = 1; i < n; i++) {
            max_profit[i] = max(max_profit[i-1], tasks[i].second);
        }
        int ans = 0;
        for (int w : worker) {
            int idx = upper_bound(tasks.begin(), tasks.end(), make_pair(w, INT_MAX)) - tasks.begin() - 1; // find the last task that can be done
            ans += idx >= 0 ? max_profit[idx] : 0;
        }
        return ans;
    }
};
// @lc code=end

