#include <bits/stdc++.h>
using namespace std;
using LL = long long;
# define min(a, b) ((a) < (b) ? (a) : (b))
# define max(a, b) ((a) > (b) ? (a) : (b))
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;

class Solution {
public:
    long long minimumCost(string source, string target, vector<string>& original, vector<string>& changed, vector<int>& cost) {
        unordered_set<string> nodes;
        unordered_map<string, unordered_map<string, LL>> g;
        for (int i = 0; i < original.size(); ++i) {
            g[original[i]][changed[i]] = min(g[original[i]][changed[i]], cost[i]);
            nodes.insert(original[i]);
            nodes.insert(changed[i]);
        }
        for (auto& node : nodes) {
            g[node][node] = 0;
        }
        for (auto& u : nodes) {
            for (auto& v : nodes) {
                if (!g[u].count(v)) {
                    g[u][v] = LLONG_MAX;
                }
            }
        }
        // Floyd-Warshall
        vector<string> sorted_nodes(nodes.begin(), nodes.end());
        sort(sorted_nodes.begin(), sorted_nodes.end());
        for (auto& k : sorted_nodes) {
            for (auto& i : sorted_nodes) {
                for (auto& j : sorted_nodes) {
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
                }
            }
        }
        LL max_len = 0;
        for (auto& node : nodes) {
            max_len = max(max_len, (LL)node.size());
        }
        // DP
        // dp[i] 表示 修改 source[:i] 為 target[:i] 的最小代價
        int n = source.size();
        vector<LL> dp(n + 1, LLONG_MAX);
        dp[0] = 0;
        for (LL i = 1; i <= n; ++i) {
            if (source[i - 1] == target[i - 1]) {
                dp[i] = dp[i - 1];
            }
            for (LL j = max(0, i - max_len); j < i; ++j) { // 長度
                string u = source.substr(j, i - j);
                string v = target.substr(j, i - j);
                if (g.count(u) && g[u].count(v)) {
                    dp[i] = min(dp[i], dp[j] + g[u][v]);
                }
            }
        }
        return dp[n] != INT_MAX ? dp[n] : -1;
    }
};