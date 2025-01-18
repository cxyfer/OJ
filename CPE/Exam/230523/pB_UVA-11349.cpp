#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, kase=1, n;
    char t1, t2;
    cin >> t;
    while (t--) {
        cin >> t1 >> t2 >> n;
        // Read matrix and check if any element is negative
        vector<vector<LL>> mat(n, vector<LL>(n));
        bool flag = true;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> mat[i][j];
                if (mat[i][j] < 0) flag = false;
            }
        }
        // Check if the matrix is symmetric
        for (int i = 0; i < (n + 1) / 2 && flag; ++i) {
            for (int j = 0; j < n && flag; ++j) {
                if (mat[i][j] != mat[n - i - 1][n - j - 1])
                    flag = false;
            }
        }
        // Output
        cout << "Test #" << kase++ << ": ";
        if (flag) cout << "Symmetric." << endl;
        else cout << "Non-symmetric." << endl;
    }
    return 0;
}