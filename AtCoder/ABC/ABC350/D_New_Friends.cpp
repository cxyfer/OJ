#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 2e5 + 10;
#define endl '\n'

bool visited[N];
vector<int> g[N];

int dfs(int u, int fa) {
    visited[u] = true;
    int res = 1;
    for (int v : g[u]) {
        if (v == fa) continue;
        if (!visited[v]) {
            res += dfs(v, u);
        }
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m; cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    LL ans = -m, res = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            res = dfs(i, -1);
            ans += res * (res - 1LL) / 2LL;
        }
    }
    cout << ans << endl;
    return 0;
}