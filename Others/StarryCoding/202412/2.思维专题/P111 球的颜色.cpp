#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, c, x, y;
    cin >> n >> q;
    vector<unordered_set<int>> S(n);
    for (int i = 0; i < n; ++i) {
        cin >> c;
        S[i].insert(c);
    }
    while (q--) {
        cin >> x >> y;
        --x, --y;
        // 啟發式合併，永遠把小集合合併到大集合
        if (S[x].size() > S[y].size()) swap(S[x], S[y]);
        for (int c : S[x]) S[y].insert(c);
        S[x].clear();
        cout << S[y].size() << endl;
    }
    return 0;
}