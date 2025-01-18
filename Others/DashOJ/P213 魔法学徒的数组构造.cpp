#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    vector<int> ans(n, 0);
    set<int> vis;
    for (int i = 0; i < n; i++) {
        int tgt = (i + 1) - (A[i] % (i + 1));
        while (vis.count(tgt)) tgt += (i + 1);
        vis.insert(tgt);
        ans[i] = tgt;
    }

    for (int i = 0; i < n; i++) cout << ans[i] << " \n"[i == n - 1];
    return 0;
}