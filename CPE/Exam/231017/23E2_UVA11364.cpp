#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> X(n);
        int mx = INT_MIN, mn = INT_MAX;
        for (int i = 0; i < n; i++) {
            cin >> X[i];
            mx = max(mx, X[i]);
            mn = min(mn, X[i]);
        }
        cout << (mx - mn) * 2 << endl;
    }
    return 0;
}