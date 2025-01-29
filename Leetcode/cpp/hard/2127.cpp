/*
 * @lc app=leetcode.cn id=2127 lang=cpp
 *
 * [2127] 参加会议的最多员工数
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
 public:
  int maximumInvitations(vector<int>& favorite) {
    int n = favorite.size();
    vector<int> ind(n);
    for (int f : favorite) ind[f]++;

    vector<vector<int>> rg(n);
    queue<int> q;
    for (int i = 0; i < n; ++i)
      if (ind[i] == 0) q.push(i);

    while (!q.empty()) {
      int u = q.front();
      q.pop();
      int v = favorite[u];
      rg[v].push_back(u);
      ind[v]--;
      if (ind[v] == 0) q.push(v);
    }

    auto rdfs = [&](auto&& rdfs, int u) -> int {
      int res = 1;
      for (int v : rg[u]) 
        res = max(res, rdfs(rdfs, v) + 1);
      return res;
    };

    int max_ring = 0, sum_chain = 0;
    for (int u = 0; u < n; ++u) {
      if (ind[u] == 0) continue;

      vector<int> rings = {u};
      int v = favorite[u];
      while (v != u) {
        rings.push_back(v);
        v = favorite[v];
      }
      for (int v : rings) ind[v] = 0;

      if (rings.size() == 2)
        sum_chain += rdfs(rdfs, u) + rdfs(rdfs, favorite[u]);
      else
        max_ring = max(max_ring, (int)rings.size());
    }
    return max(max_ring, sum_chain);
  }
};
// @lc code=end