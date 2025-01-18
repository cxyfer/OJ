#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> A(n + 1);
        for (int i = 1; i <= n; i++) cin >> A[i];
        vector<LL> s(n + 1, 0);
        for (int i = 2; i <= n; i++) {
            s[i] = s[i - 1] + (A[i] == A[i - 1] ? A[i] : 0);
        }
        vector<LL> f(n + 1, 0);
        unordered_map<int, int> lst;
        for (int i = 1; i <= n; i++) {
            f[i] = f[i - 1];
            if (lst.find(A[i]) != lst.end()) {
                f[i] = max(f[i], f[lst[A[i]] + 1] + A[i] + s[i] - s[lst[A[i]] + 1]);
            }
            lst[A[i]] = i;
        }
        cout << f[n] << endl;
    }
    return 0;
}