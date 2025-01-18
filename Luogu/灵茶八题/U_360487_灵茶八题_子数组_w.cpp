#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    // int ans = 0;
    // for (int i = 0; i < n; i++) {
    //     if ((i + 1) * (n - i) & 1) {
    //         ans ^= A[i];
    //     }
    // }
    // cout << ans << endl;
    if (n & 1) {
        int ans = 0;
        for (int i = 0; i < n; i += 2) {
            ans ^= A[i];
        }
        cout << ans << endl;
    } else {
        cout << 0 << endl;
    }
    return 0;
}