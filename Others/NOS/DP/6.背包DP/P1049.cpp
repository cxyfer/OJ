#include <bits/stdc++.h>
using namespace std;
const int MAX_V = 2e4 + 5;
#define endl '\n'

void solve() {
    int V, n;
    cin >> V >> n;
    vector<int> A(n);
    for (auto& x : A) cin >> x;

    bitset<MAX_V> f = 1;
    for (int x : A) f |= (f << x);
    for (int v = V; v >= 0; v--) {
        if (f[v]) {
            cout << V - v << endl;
            break;
        }
    }
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}