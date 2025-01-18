#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n);
    for (auto &x: A) cin >> x;
    int res = 0;
    for (auto &x: A) res ^= x;
    if (res == 0) {
        cout << "lose" << endl;
    } else {
        int idx = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            if ((A[i] ^ res) < A[i]) {
                idx = i + 1;
                ans = A[i] - (A[i] ^ res);
                A[i] = A[i] ^ res;
                break;
            }
        }
        cout << ans << " " << idx << endl;
        for (auto x: A) cout << x << " ";
        cout << endl;
    }
    return 0;
}