#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e5 + 5;
#define endl '\n'

int a[N];
LL s[N];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, q;
    cin >> t;
    while (t--) {
        cin >> n >> q;
        for (int i = 1; i <= n; i++) cin >> a[i];
        for (int i = 1; i <= n; i++) s[i] = s[i - 1] + a[i];
        while (q--) {
            int l, r;
            cin >> l >> r;
            cout << s[r] - s[l - 1] << endl;
        }
    }
    return 0;
}