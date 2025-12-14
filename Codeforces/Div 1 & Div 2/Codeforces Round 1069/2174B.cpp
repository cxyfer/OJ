#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

void solve() {
    int n, k;
    cin >> n >> k;
    vector<int> A(n);
    for (auto &x : A) cin >> x;

    vector<pair<int, int>> B;
    for (int i = 0; i < n; i++)
        if (B.empty() || A[i] > B.back().second)
            B.emplace_back(i, A[i]);
    int m = B.size();

    vector<vector<int>> f(k + 1, vector<int>(k + 1, -INF)), nf(k + 1, vector<int>(k + 1, -INF));
    for (int s = 0; s <= k; s++) f[0][s] = 0;
    for (auto& [idx, x] : B) {
        for (int s = 0; s <= k; s++) {
            int mx = -INF;  // 維護 max(f[v][s - u] - v * (n - idx) for v in range(u))
            for (int u = 0; u <= k; u++) {
                nf[u][s] = f[u][s];
                int ns = s - u;
                if (u > x || ns < 0) continue;
                nf[u][ns] = max(nf[u][ns], mx + u * (n - idx));
                mx = max(mx, nf[u][s] - u * (n - idx));
            }
        }
        swap(f, nf);
    }
    int ans = -INF;
    for (int u = 0; u <= k; u++)
        for (int s = 0; s <= k; s++)
            ans = max(ans, f[u][s]);
    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}