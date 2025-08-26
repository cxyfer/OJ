#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

vector<int> getLIS(vector<int> A) {
    vector<int> f, res;
    for (int x : A) {
        auto it = lower_bound(f.begin(), f.end(), x);
        res.push_back(it - f.begin() + 1);
        if (it == f.end()) f.push_back(x);
        else *it = x;
    }
    return res;
}

void solve() {
    int n; cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) cin >> A[i];

    auto pre = getLIS(A);
    reverse(A.begin(), A.end());
    auto suf = getLIS(A);
    reverse(suf.begin(), suf.end());
    int ans = 0;
    for (int i = 0; i < n; ++i) ans = max(ans, pre[i] + suf[i] - 1);
    cout << n - ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    solve();
    return 0;
}