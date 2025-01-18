#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }
        vector<int> f(n + 2, 0);
        f[n + 1] = INF;
        for (int i = n - 1; i >= 0; i--) {
            f[i] = min(1 + f[i + 1], f[min(n + 1, i + A[i] + 1)]);
        }
        cout << f[0] << endl;
    }
    return 0;
}