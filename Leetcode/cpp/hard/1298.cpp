/*
 * @lc app=leetcode.cn id=1298 lang=cpp
 * @lcpr version=30204
 *
 * [1298] 你能从盒子里获得的最大糖果数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        int n = status.size();
        vector<bool> hasBox(n, false), canOpen(n, false), visited(n, false);
        queue<int> q;
        for (int u : initialBoxes) hasBox[u] = true;
        for (int u = 0; u < n; u++) {
            canOpen[u] = status[u] == 1;
            if (hasBox[u] && canOpen[u]) {
                visited[u] = true;
                q.push(u);
            }
        }
        int ans = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            ans += candies[u];
            for (int v : containedBoxes[u]) {
                hasBox[v] = true;
                if (hasBox[v] && canOpen[v] && !visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
            for (int v : keys[u]) {
                canOpen[v] = true;
                if (hasBox[v] && canOpen[v] && !visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,0,1,0]\n[7,5,4,100]\n[[],[],[1],[]]\n[[1,2],[3],[],[]]\n[0]\n
// @lcpr case=end

// @lcpr case=start
// [1,0,0,0,0,0]\n[1,1,1,1,1,1]\n[[1,2,3,4,5],[],[],[],[],[]]\n[[1,2,3,4,5],[],[],[],[],[]]\n[0]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1]\n[100,1,100]\n[[],[0,2],[]]\n[[],[],[]]\n[1]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n[100]\n[[]]\n[[]]\n[]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1]\n[2,3,2]\n[[],[],[]]\n[[],[],[]]\n[2,1,0]\n
// @lcpr case=end

 */

