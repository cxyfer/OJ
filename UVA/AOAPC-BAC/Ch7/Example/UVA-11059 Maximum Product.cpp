#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, kase = 1;
    while (cin >> n) {
        vector<int> A(n);
        for (int i = 0; i < n; i++) cin >> A[i];
        LL ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                LL prod = 1;
                for (int k = i; k <= j; k++) {
                    prod *= A[k];
                }
                ans = max(ans, prod);
            }
        }
        cout << "Case #" << kase++ << ": The maximum product is " << ans << "." << endl;
        cout << endl;
    }
    return 0;
}