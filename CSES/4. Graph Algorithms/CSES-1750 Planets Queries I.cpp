#include <bits/stdc++.h>
using namespace std;
const int M = 30;  // MAX_K = 1e9
#define endl '\n'

void solve() {
    int n, q, v;
    cin >> n >> q;
    vector<vector<int>> pa(n, vector<int>(M, -1));
    for (int u = 0; u < n; u++) {
        cin >> v;
        pa[u][0] = v - 1;
    }
    // 用倍增法更新 pa
    for (int i = 0; i < M - 1; i++)
        for (int u = 0; u < n; u++)
            if (pa[u][i] != -1) pa[u][i + 1] = pa[pa[u][i]][i];

    while (q--) {
        int u, k;
        cin >> u >> k;
        u -= 1;
        for (; k; k &= k - 1)
            u = pa[u][bit_width(static_cast<unsigned>(k & -k)) - 1];
        cout << u + 1 << endl;
    }
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}