#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {
    int n, q, fa;
    cin >> n >> q;
    int m = bit_width(static_cast<unsigned>(n));
    vector<vector<int>> pa(n, vector<int>(m, -1));
    for (int u = 1; u < n; u++) {
        cin >> fa;
        pa[u][0] = fa - 1;
    }
    // 用倍增法更新 pa
    for (int i = 0; i < m - 1; i++)
        for (int u = 0; u < n; u++)
            if (pa[u][i] != -1) pa[u][i + 1] = pa[pa[u][i]][i];

    while (q--) {
        int u, k;
        cin >> u >> k;
        u -= 1;
        for (; k && u != -1; k &= k - 1)
            u = pa[u][bit_width(static_cast<unsigned>(k & -k)) - 1];
        cout << (u != -1 ? u + 1 : -1) << endl;
    }
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
#ifdef LOCAL
    ifstream fin("input.txt");
    cin.rdbuf(fin.rdbuf());
#endif
    solve();
    return 0;
}