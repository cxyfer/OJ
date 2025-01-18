#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MX = 1e6 + 5;
#define endl '\n'

LL cnt[MX], s[MX];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        cnt[x]++;
    }
    for (int i = 1; i < MX; i++) s[i] = s[i - 1] + cnt[i];
    LL ans = 0;
    for (int i = 1; i < MX; i++) {
        ans += cnt[i] * (cnt[i] - 1) / 2;
        for (int j = i; j < MX; j += i) {
            int l = (j == i ? i + 1 : j);
            int r = min(MX - 1, j + i - 1);
            ans += cnt[i] * (j / i) * (s[r] - s[l - 1]);
        }
    }
    cout << ans << endl;
    return 0;
}