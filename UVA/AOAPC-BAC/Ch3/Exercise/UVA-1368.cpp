#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, m;
    string mp = "ACGT"; // in lexicographical order
    cin >> t;
    while (t--) {
        cin >> n >> m;
        string s[n];
        for (int i = 0; i < n; i++) cin >> s[i];
        string ans = "";
        int err = 0;
        for (int j = 0; j < m; j++) {
            int cnt[4] = {0};
            for (int i = 0; i < n; i++) cnt[mp.find(s[i][j])]++;
            int idx = 0; // index of max value
            for (int k = 1; k < 4; k++) if (cnt[k] > cnt[idx]) idx = k;
            ans += mp[idx];
            err += n - cnt[idx];
        }
        cout << ans << endl << err << endl;
    }
    return 0;
}