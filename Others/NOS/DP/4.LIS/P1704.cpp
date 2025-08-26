/*
P1704 寻找最优美做题曲线
https://www.luogu.com.cn/problem/P1704
分段求 LIS
*/
#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

void solve() {
    int N, K;
    cin >> N >> K;
    vector<int> P(K + 2), C(N + 2);
    for (int i = 1; i <= K; ++i) cin >> P[i];
    for (int i = 1; i <= N; ++i) cin >> C[i];
    P[0] = 0, P[K + 1] = N + 1;
    C[0] = 0, C[N + 1] = INF;
    sort(P.begin(), P.end());

    for (auto [a, b] : views::pairwise(P)) {
        if (C[a] >= C[b]) {
            cout << "impossible" << endl;
            return;
        }
    }

    int ans = K;
    vector<int> f;
    for (auto [l, r] : views::pairwise(P)) {
        f.clear();
        for (int i = l + 1; i < r; ++i) {
            if (C[i] <= C[l] || C[i] >= C[r]) continue;
            auto it = lower_bound(f.begin(), f.end(), C[i]);
            if (it == f.end())
                f.push_back(C[i]);
            else
                *it = C[i];
        }
        ans += f.size();
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    solve();
    return 0;
}