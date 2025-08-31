#include <bits/stdc++.h>
#include <ranges>
using namespace std;
#define endl '\n'

void solve() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (auto& x : A) cin >> x;
    int B = bit_width(static_cast<unsigned>(ranges::max(A)));
    int U = 1 << B;

    vector<pair<int, int>> f(U, {-1, -1});
    auto update = [&](int s, int i) {
        if (i > f[s].first)
            f[s] = {i, f[s].first};
        else if (i > f[s].second)
            f[s] = {f[s].first, i};
    };

    for (int i = 0; i < n; ++i) update(A[i], i);

    for (int i = 0; i < B; ++i) {
        // for (int s = U - 1; s >= 0; --s) {
        //     if ((s >> i) & 1) {
        //         update(s ^ (1 << i), f[s].first);
        //         update(s ^ (1 << i), f[s].second);
        //     }
        // }
        for (int s = 0; s < U; ++s) {
            s |= (1 << i);
            update(s ^ (1 << i), f[s].first);
            update(s ^ (1 << i), f[s].second);
        }
    }

    int ans = 0;
    for (int i = 0; i < n - 2; ++i) {
        int x = A[i];
        int s = 0;
        for (int b = B - 1; b >= 0; --b) {
            if ((x >> b) & 1) continue;
            if (f[s | (1 << b)].second > i) s |= (1 << b);
        }
        ans = max(ans, x | s);
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}