#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

vector<string> mp;

bool check(int x, int y, int r) {
    int M = mp.size(), N = mp[0].size();
    if (x < 0 || x >= M || y < 0 || y >= N) return false;
    for (int i = -r; i <= r; i++) {
        for (int j = -r; j <= r; j += 2 * r) {
            if (x + i < 0 || x + i >= M || y + j < 0 || y + j >= N)
                return false;
            if (mp[x + i][y + j] != mp[x][y]) return false;
        }
    }
    for (int j = -r; j <= r; j++) {
        for (int i = -r; i <= r; i += 2 * r) {
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
    int t, m, n, q, x, y, r;
    cin >> t;
    while (t--) {
        cin >> m >> n >> q;
        mp.resize(m);
        for (int i = 0; i < m; i++) cin >> mp[i];
        cout << m << " " << n << " " << q << endl;
        while (q--) {
            cin >> x >> y;
            r = 1;
            while (check(x, y, r)) r++;
            cout << 2 * r - 1 << endl;
        }
    }
    return 0;
}