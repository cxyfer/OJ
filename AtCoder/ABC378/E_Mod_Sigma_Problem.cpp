#include <bits/stdc++.h>
#include <atcoder/fenwicktree>
using namespace std;
using namespace atcoder;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, M; cin >> N >> M;
    vector<int> A(N);
    vector<LL> s(N + 1);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        s[i + 1] = (s[i] + A[i]) % M;
    }

    fenwick_tree<LL> bit(M);
    bit.add(0, 1);
    LL ans = 0, s_sl= 0;
    for (int r = 1; r <= N; r++) {
        ans += s[r] * r - s_sl;
        ans += M * (r - bit.sum(0, s[r] + 1));
        bit.add(s[r], 1);
        s_sl += s[r];
    }
    cout << ans << endl;
    return 0;
}