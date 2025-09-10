#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N; cin >> N;

    vector<pair<int, int>> cows(N);
    for (auto &[a, b] : cows) cin >> a >> b;

    // f[s] 表示智商和為 s 時，能達到的最大情商和
    unordered_map<int, int> f;
    f[0] = 0;
    for (auto [a, b] : cows) {
        auto nf = f;
        for (auto [s, t] : f) {
            int ns = s + a, nt = t + b;
            if (nf.find(ns) == nf.end() || nt > nf[ns])
                nf[ns] = nt;
        }
        f = move(nf);
    }

    int ans = 0;
    for (auto [s, t] : f)
        if (s >= 0 && t >= 0) ans = max(ans, s + t);
    cout << ans << endl;

    // int s1 = 0, s2 = 0;
    // for (auto [a, b] : cows)
    //     if (a >= 0) s1 += a;
    //     else s2 -= a;

    // // f[j] 表示智商和為 j 時，能達到的最大情商和
    // vector<int> f(s1 + s2 + 1, INT_MIN / 2);
    // f[0 + s2] = 0;
    // for (auto [a, b] : cows)
    //     if (a >= 0)
    //         for (int j = s1 + s2; j >= a; --j)
    //             f[j] = max(f[j], f[j - a] + b);
    //     else
    //         for (int j = 0; j - a <= s1 + s2; ++j)
    //             f[j] = max(f[j], f[j - a] + b);

    // int ans = 0;
    // for (int j = s2; j <= s1 + s2; ++j)
    //     if (f[j] >= 0) ans = max(ans, (j - s2) + f[j]);
    // cout << ans << endl;
    return 0;
}