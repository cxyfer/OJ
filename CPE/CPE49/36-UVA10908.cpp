#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

bool check(vector<string> &mp, int x, int y, int r){
    int M = mp.size(), N = mp[0].size();
    if (x < 0 || y < 0 || x >= M || y >= N) return false;
    for (int i=-r; i<=r; i++) {
        for (int j=-r; j<=r; j++) {
            if (x+i < 0 || y+j < 0 || x+i >= M || y+j >= N) return false;
            if (mp[x+i][y+j] != mp[x][y]) return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, m, n, q, qx, qy;
    cin >> t;
    while (t--) {
        cin >> m >> n >> q;
        vector<string> mp(m);
        for (int i=0; i<m; i++) {
            cin >> mp[i];
        }
        cout << m << " " << n << " " << q << endl;
        while (q--) {
            int x, y;
            cin >> x >> y;
            int c = 0;
            while (check(mp, x, y, c)) {
                c++;
            }
            cout << 2*c-1 << endl;
        }   
    }
    return 0;
}