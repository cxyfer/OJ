#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N; cin >> N;

    vector<pair<int, int>> cows(N);
    for (int i = 0; i < N; ++i) cin >> cows[i].first >> cows[i].second;

    // f[s] 表示智商和為 s 時，能達到的最大情商和
    unordered_map<int, int> f;
    f[0] = 0;
    for (auto [s_i, f_i] : cows) {
        auto nf = f;
        for (auto [s_tot, f_tot] : f) {
            int new_s = s_tot + s_i, new_f = f_tot + f_i;
            if (nf.find(new_s) == nf.end() || new_f > nf[new_s])
                nf[new_s] = new_f;
        }
        f = move(nf);
    }

    int ans = 0;
    for (auto [s_tot, f_tot] : f)
        if (s_tot >= 0 && f_tot >= 0) ans = max(ans, s_tot + f_tot);
    cout << ans << endl;
    return 0;
}