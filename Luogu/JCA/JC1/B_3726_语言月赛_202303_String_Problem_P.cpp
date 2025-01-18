#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, op, x, y, i;
    cin >> n >> q;
    vector<string> S(n + 1);
    for (int i = 1; i <= n; ++i) cin >> S[i];
    while (q--) {
        cin >> op;
        if (op == 1) {
            cin >> x >> y >> i;
            S[y] = S[y].substr(0, i) + S[x] + S[y].substr(i);
        } else {
            cin >> i;
            cout << S[i] << endl;
        }
    }
    return 0;
}