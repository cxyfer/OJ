#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, Q, q_i, r_i, t_j, d_j;
    cin >> N;
    vector<pair<int, int>> garbages(N);
    for (int i = 0; i < N; i++) {
        cin >> garbages[i].first >> garbages[i].second;
    }
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> t_j >> d_j;
        q_i = garbages[t_j - 1].first;
        r_i = garbages[t_j - 1].second;
        if (d_j % q_i == r_i) {
            cout << d_j << endl;
        } else {
            cout << d_j + ((r_i - d_j) % q_i + q_i) % q_i << endl;
        }
    }
    return 0;
}