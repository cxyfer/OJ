#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
#define endl '\n'

void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> A(n);
    for (auto& x : A) cin >> x;
    vector<array<int, 3>> queries(m);
    for (auto& [d, l, r] : queries) {
        cin >> d >> l >> r;
        --l;
        --r;
    }

    vector<i64> diff(n + 1);
    for (auto& [d, l, r] : queries) {
        diff[l] += d;
        diff[r + 1] -= d;
    }

    i64 s = 0;
    int k = m - 1;
    for (int i = 0; i < n; i++) {
        s += diff[i];
        while (k >= 0 && s > A[i]) {
            auto& [v, l, r] = queries[k];
            diff[l] -= v;
            diff[r + 1] += v;
            if (l <= i && i <= r) {
                s -= v;
            }
            k -= 1;
        }
        if (s > A[i]) break;
    }

    // 有不能被滿足的需求
    if (k < m - 1) {
        cout << -1 << endl;
        // k + 1 是第一個不能被滿足的需求，轉換為 1-index 後是 k + 2
        cout << k + 2 << endl;
    } else {
        cout << 0 << endl;
    }
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}