/*
pF_UVA-10690 Expression Again
https://vjudge.net/problem/UVA-13242
Prefix Sum

不確定題目中的 lowest numbers 是指起始的下標最小還是數量最少，但兩種似乎都能過
*/

#include <bits/stdc++.h>
using namespace std;
using LL = long long;
using pii = pair<int, int>;
#define endl '\n'

void solve() {
    int V, T, N;
    cin >> V >> T;
    cin >> N;
    vector<pii> jars(N);
    for (auto& [v, t] : jars) cin >> v >> t;

    vector<LL> sv(N + 1), sw(N + 1);
    for (int i = 0; i < N; i++) {
        sv[i + 1] = sv[i] + jars[i].first;
        sw[i + 1] = sw[i] + jars[i].first * jars[i].second;
    }

    pii ans = {-1, -1};
    double mnd = DBL_MAX;
    for (int i = 0; i < N; i++) {
        for (int j = i; j < N; j++) {
            LL v = sv[j + 1] - sv[i], w = sw[j + 1] - sw[i];
            // V / 2 <= v <= V && T - 5 <= w / v <= T + 5
            if ((V <= 2 * v && v <= V) && (T - 5) * v <= w && w <= (T + 5) * v) {
                double d = abs(1.0 * w / v - T);
                if (d < mnd) {
                    mnd = d;
                    ans = {i, j};
                }
                // else if (d == mnd && j - i < ans.second - ans.first) {
                //     ans = {i, j};
                // }
            }
        }
    }

    if (ans.first == -1 && ans.second == -1)
        cout << "Not possible" << endl;
    else
        cout << ans.first << " " << ans.second << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t; cin >> t;
    while (t--) solve();
    return 0;
}