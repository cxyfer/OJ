#include <bits/stdc++.h>
using namespace std;
const int N = 3660;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, p, h, days[N+1], ans;
    cin >> t;
    while (t--) {
        cin >> n >> p;
        memset(days, 0, sizeof(days));
        for (int i=0; i<p; i++) {
            cin >> h;
            for (int j=h; j<=n; j+=h) {
                days[j] = 1;
            }
        }
        ans = 0;
        for (int i=1; i<=n; i++) {
            if (i % 7 == 6 || i % 7 == 0) continue;
            ans += days[i];
        }
        cout << ans << endl;
    }
    return 0;
}