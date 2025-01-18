#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 1e18;
#define endl '\n'

struct Hero {
    int cost, w;
};

struct Group {
    int u, v, w;
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, C, M, cost, u, v, w;
    cin >> N >> C >> M;
    vector<Hero> heroes(N);
    for (int i = 0; i < N; i++) {
        cin >> cost >> w;
        heroes[i] = {cost, w};
    }
    vector<Group> groups;
    vector<bool> is_pair(N, false);
    for (int i = 0; i < M; i++) {
        cin >> u >> v >> w;
        u--; v--;
        is_pair[u] = true;
        is_pair[v] = true;
        groups.push_back({u, v, w});
    }
    for (int i = 0; i < N; i++) {
        if (!is_pair[i]) {
            groups.push_back({i, i, 0});
        }
    }
    int n = groups.size();
    vector<vector<vector<LL>>> memo(n + 1, vector<vector<LL>>(C + 1, vector<LL>(5, -INF)));
    auto dfs = [&](auto &&dfs, int i, int j, int k) -> LL {
        if (j > C || k > 4) return -INF;
        if (i == n || j == C || k == 4) return 0;
        LL &res = memo[i][j][k];
        if (res != -INF) return res;
        res = dfs(dfs, i + 1, j, k);
        auto [u, v, w] = groups[i];
        if (u != v) {
            auto [cost_u, w_u] = heroes[u];
            auto [cost_v, w_v] = heroes[v];
            res = max({res, 
                      dfs(dfs, i + 1, j + cost_u, k + 1) + w_u,
                      dfs(dfs, i + 1, j + cost_v, k + 1) + w_v,
                      dfs(dfs, i + 1, j + cost_u + cost_v, k + 2) + w_u + w_v + w});
        } else {
            auto [cost, w] = heroes[u];
            res = max(res, dfs(dfs, i + 1, j + cost, k + 1) + w);
        }
        return res;
    };
    cout << dfs(dfs, 0, 0, 0) << endl;
    return 0;
}