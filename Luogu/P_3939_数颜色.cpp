#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> C(n + 1);
    unordered_map<int, vector<int>> pos;
    for (int i = 1; i <= n; i++) {
        cin >> C[i];
        pos[C[i]].push_back(i);
    }
    int op, l, r, c, x;
    while (q--) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> c;
            auto it1 = lower_bound(pos[c].begin(), pos[c].end(), l);
            auto it2 = upper_bound(pos[c].begin(), pos[c].end(), r);
            cout << it2 - it1 << endl;
        } else {
            cin >> x;
            if (C[x] == C[x + 1]) continue;
            auto it1 = lower_bound(pos[C[x]].begin(), pos[C[x]].end(), x);
            auto it2 = lower_bound(pos[C[x + 1]].begin(), pos[C[x + 1]].end(), x + 1);
            swap(*it1, *it2);
            swap(C[x], C[x + 1]);
        }
    }
    return 0;
}