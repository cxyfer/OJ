/*
對於一個度數皆為 3 的連通分量，可以計算他相鄰的點中度數為 2 的點的數量 cnt
在這些度數為 2 的點中，任選兩個配對，即可滿足題目要求，故這個連通分量的貢獻為 cnt * (cnt - 1) // 2
可以用 BFS 或 DFS 找到所有度數皆為 3 的連通分量
*/

#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N; cin >> N;
    vector<pair<int, int>> edges(N - 1);
    for (int i = 0; i < N - 1; i++) {
        cin >> edges[i].first >> edges[i].second;
    }
    vector<vector<int>> g(N + 1);
    vector<int> deg(N + 1);
    for (auto [u, v] : edges) {
        g[u].push_back(v);
        g[v].push_back(u);
        deg[u] += 1;
        deg[v] += 1;
    }
    vector<bool> vis(N + 1);
    auto dfs = [&](auto dfs, int u) -> int {
        if (deg[u] != 3 || vis[u]) return 0;
        vis[u] = true;
        int cnt = 0;
        for (int v : g[u]) {
            if (deg[v] == 2) cnt += 1;
            else if (deg[v] == 3 && !vis[v]) cnt += dfs(dfs, v);
        }
        return cnt;
    };
    LL ans = 0;
    for (int i = 1; i <= N; i++) {
        if (deg[i] != 3 || vis[i]) continue;
        int cnt = dfs(dfs, i);
        ans += cnt * (cnt - 1LL) / 2;
    }
    cout << ans << endl;
    return 0;
}