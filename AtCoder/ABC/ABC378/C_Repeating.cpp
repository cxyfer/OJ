#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, x; cin >> N;
    unordered_map<int, int> pos;
    vector<int> ans(N, -1);
    for (int i = 0; i < N; i++) {
        cin >> x;
        ans[i] = (pos.find(x) == pos.end() ? -1 : pos[x]);
        pos[x] = i + 1;
    }
    for (int i = 0; i < N; i++) {
        cout << ans[i] << ' ';
    }
    cout << endl;
    return 0;
}