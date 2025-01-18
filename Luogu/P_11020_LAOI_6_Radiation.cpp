#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, m, k, r, sz;
    cin >> t;
    while (t--) {
        cin >> n >> m >> k;
        sz = min(n, m);
        r = max(0, k - sz);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == j && k) {
                    cout << 'S';
                    k--;
                }
                else if (r) {
                    cout << 'S';
                    r--;
                }
                else cout << '.';
            }
            cout << endl;
        }
    }
    return 0;
}