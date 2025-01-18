#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> A(n);
        LL s = 0;
        map<LL, bool> seen;
        seen[0] = true;
        bool flag = false;
        for (int i = 0; i < n; ++i) {
            cin >> A[i];
            s += (i & 1)? -A[i]: A[i];
            if (seen[s]) {
                flag = true;
            }
            seen[s] = true;
        }
        cout << (flag? "YES": "NO") << "\n";
    }
    return 0;
}