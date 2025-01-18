#include <bits/stdc++.h>
using namespace std;
const int N = 10;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, kase=1, n, m, x, mat[N][N];
    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> x;
            for (int j = n-1; j >= 0; j--) {
                mat[i][j] = x % 10;
                x /= 10;
            }
        }
        cin >> m; // number of operations
        int a, b;
        string op;
        while (m--) {
            cin >> op;
            if (op == "row") {
                cin >> a >> b;
                for (int i = 0; i < n; i++) {
                    swap(mat[a-1][i], mat[b-1][i]);
                }
            } else if (op == "col") {
                cin >> a >> b;
                for (int i = 0; i < n; i++) {
                    swap(mat[i][a-1], mat[i][b-1]);
                }
            } else if (op == "inc") {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        mat[i][j] = (mat[i][j] + 1) % 10;
                    }
                }
            } else if (op == "dec") {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        mat[i][j] = (mat[i][j] + 9) % 10;
                    }
                }
            } else if (op == "transpose") {
                for (int i = 0; i < n; i++) {
                    for (int j = i+1; j < n; j++) {
                        swap(mat[i][j], mat[j][i]);
                    }
                }
            }
        }
        cout << "Case #" << kase++ << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << mat[i][j];
            }
            cout << endl;
        }
        cout << endl; // print a blank line after each test case
    }
    return 0;
}