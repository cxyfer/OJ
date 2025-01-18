/*
    解法：根號分治 / Bitset / 啟發式合併

    1. 啟發式合併
    Ref: https://www.bilibili.com/video/BV1TZ421H7xo/
    時間複雜度：O(n log n) ，每次合併會使大小至少增加一倍，因此對於每個點，最多只會有 log n 次合併
*/

#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 998244353;
const int N = 1e5 + 5;
#define endl '\n'

// Disjoint Set
int pa[N], sz[N];
int find(int x) {
    return pa[x] == x ? x : pa[x] = find(pa[x]);
}

// Graph
int fa[N] = {0};
vector<int> g[N];
void dfs(int u) {
    for (int v : g[u]) {
        if (v == fa[u]) continue;
        fa[v] = u;
        dfs(v);
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q; cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        pa[i] = i;
        sz[i] = 1;
    }
    LL ans = 0;
    while (q--) {
        int a, b, c; cin >> a >> b >> c;
        int op = 1 + a * (1LL + ans) % MOD % 2;
        int x = 1 + b * (1LL + ans) % MOD % n;
        int y = 1 + c * (1LL + ans) % MOD % n;
        if (op == 1) {
            if (sz[find(x)] > sz[find(y)]) swap(x, y);
            sz[find(y)] += sz[find(x)];
            pa[find(x)] = find(y);
            g[x].push_back(y);
            g[y].push_back(x);
            fa[x] = y;
            dfs(x);
        } else {
            if (fa[x] != 0 && fa[x] == fa[y]) {
                ans = fa[x];
            } else if (fa[fa[x]] == y) {
                ans = fa[x];
            } else if (fa[fa[y]] == x) {
                ans = fa[y];
            } else {
                ans = 0;
            }
            cout << ans << endl;
        }
    }
    return 0;
}
