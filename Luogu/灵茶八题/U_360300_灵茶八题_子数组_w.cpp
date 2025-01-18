#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    LL ans = 0;
    for (int i = 0; i < n; i++) {
        ans += 1LL * A[i] * (i + 1) * (n - i);
    }
    cout << ans << endl;
    return 0;
}