/*
 * @lc app=leetcode.cn id=1353 lang=cpp
 * @lcpr version=30204
 *
 * [1353] 最多可以参加的会议数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        int ans = 0, mx = 0;
        unordered_map<int, vector<int>> mp; 
        for (auto &e : events) {
            mp[e[0]].push_back(e[1]);
            mx = max(mx, e[1]);
        }
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int d = 1; d <= mx; d++) {
            while (!pq.empty() && pq.top() < d)
                pq.pop();
            if (mp.count(d)) {
                for (auto &e : mp[d])
                    pq.push(e);
            }
            if (!pq.empty()) {
                pq.pop();
                ans++;
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,2],[2,3],[3,4]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2],[2,3],[3,4],[1,2]]\n
// @lcpr case=end

 */

