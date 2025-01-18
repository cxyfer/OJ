#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e4 + 5;
#define endl '\n'

int ans;
vector<vector<int>> g(N);
vector<int> marbles(N);

// pair<int, int> dfs(int u, int fa){
//     int p = 1, q = marbles[u]; // (need, have)
//     for (int v : g[u]){
//         if (v == fa) continue;
//         pair<int, int> res = dfs(v, u);
//         p += res.first;
//         q += res.second;
//     }
//     ans += abs(p - q);
//     return {p, q};
// }

int dfs(int u, int fa){ // 正數表示多餘，負數表示缺少
    int res = marbles[u] - 1;
    for (int v : g[u]){
        if (v == fa) continue;
        int res_v = dfs(v, u);
        ans += abs(res_v);
        res += res_v;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, d, u, v;
    while (cin >> n && n){
        ans = 0;
        for (int i = 1; i <= n; ++i) g[i].clear();
        for (int i = 1; i <= n; ++i){
            cin >> u >> m >> d;
            marbles[u] = m;
            for (int j = 0; j < d; ++j){
                cin >> v;
                g[u].push_back(v);
                g[v].push_back(u);
            }
        }
        dfs(1, 0);
        cout << ans << endl;
    }
    return 0;
}