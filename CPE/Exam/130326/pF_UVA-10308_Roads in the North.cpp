/*
    樹形 DP ，求直徑
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string line;
    while (getline(cin, line)) {
        int u, v, w;
        unordered_map<int, vector<pair<int, int>>> g;
        while (true) {
            if (line.empty()) break;
            stringstream ss(line);
            ss >> u >> v >> w;
            g[u].emplace_back(v, w);
            g[v].emplace_back(u, w);
            getline(cin, line);
        }

        int ans = 0;
        function<int(int, int)> dfs = [&](int u, int fa) -> int {
            int res1 = 0, res2 = 0;
            for (auto &[v, w] : g[u]) {
                if (v == fa) continue;
                int cur = w + dfs(v, u);
                if (cur > res1) {
                    res2 = res1;
                    res1 = cur;
                }
                else if (cur > res2) {
                    res2 = cur;
                }
            }
            ans = max(ans, res1 + res2);
            return res1;
        };
        dfs(1, -1);
        cout << ans << endl;
    }
    return 0;
}