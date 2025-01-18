#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, tc=1, n;
    char t1, t2;
    cin >> t;
    while (t--) {
        cin >> t1 >> t2 >> n;
        vector<vector<LL>> A(n, vector<LL>(n));
        bool flag = false;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> A[i][j];
                if (A[i][j] < 0) flag = true;
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (A[i][j] != A[n - i - 1][n - j - 1]) flag = true;
            }
            if (flag) break;
        }
        cout << "Test #" << tc++ << ": ";
        if (flag) cout << "Non-symmetric." << endl;
        else cout << "Symmetric." << endl;
    }
    return 0;
}