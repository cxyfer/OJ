/*
 * @lc app=leetcode.cn id=502 lang=cpp
 *
 * [502] IPO
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        vector<pair<int, int>> projects;
        for (int i = 0; i < n; i++)
            projects.push_back({capital[i], profits[i]});
        // Sort the projects by capital in ascending order
        sort(projects.begin(), projects.end());

        int ans = w, idx = 0;
        priority_queue<int> hp;  // Max heap
        for (int i = 0; i < k; i++) {
            // Add all the projects that can be done now
            while (idx < n && projects[idx].first <= ans)
                hp.push(projects[idx++].second);
            // No project can be done
            if (hp.empty()) break;
            // Do the project with the maximum profit
            ans += hp.top();
            hp.pop();
        }
        return ans;
    }
};
// @lc code=end