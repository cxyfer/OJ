#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

bool check(vector<string> &mp, int x, int y, int r) {
    int M = mp.size(), N = mp[0].size();
    if (x < 0 || x >= M || y < 0 || y >= N) return false;
    for (int i = -r; i <= r; i++) {
        for (int j = -r; j <= r; j++) {
            if (x + i < 0 || x + i >= M || y + j < 0 || y + j >= N)
                return false;
            if (mp[x + i][y + j] != mp[x][y]) return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t, m, n, q, x, y, l, r;
    cin >> t;
    while (t--) {
        cin >> m >> n >> q;
        vector<string> mp(m);
        for (int i = 0; i < m; i++) {
            cin >> mp[i];
        }
        cout << m << " " << n << " " << q << endl;
        while (q--) {
            cin >> x >> y;
            l = 0, r = min(m, n);
            while (l <= r) {
                int mid = (l + r) / 2;
                if (check(mp, x, y, mid)) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            cout << 2 * r + 1 << endl;
        }
    }
    return 0;
}