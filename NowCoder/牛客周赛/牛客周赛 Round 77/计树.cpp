#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, u, v, k, x;
    cin >> n;
    vector<vector<int>> g(n);
    for (int i = 0; i < n-1; i++) {
        cin >> u >> v;
        u--; v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    cin >> k;
    unordered_set<int> st;
    for (int i = 0; i < k; i++) {
        cin >> x;
        st.insert(x-1);
    }

    vector<LL> cnt(n), ans(n);
    vector<bool> vis(n);
    auto dfs = [&](auto &&dfs, int u, int fa) -> void {
        vis[u] = true;
        cnt[u] = st.count(u) ? 1 : 0;
        
        for (int v : g[u]) {
            if (v == fa || vis[v]) continue;
            dfs(dfs, v, u);
            cnt[u] += cnt[v];
        }
        
        ans[u] = cnt[u] * cnt[u];
        for (int v : g[u]) {
            if (v == fa) continue;
            ans[u] -= cnt[v] * cnt[v];
        }
    };
    dfs(dfs, 0, -1);
    
    for (int i = 0; i < n; i++) {
        cout << ans[i] << (i == n-1 ? '\n' : ' ');
    }
    return 0;
}