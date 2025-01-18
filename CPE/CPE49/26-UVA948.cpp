#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 55;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, tmp, idx;
    string ans;
    cin >> t;
    vector<LL> fib = {0, 1};
    while (fib[fib.size()-1] < 1e8) {
        fib.push_back(fib[fib.size()-1] + fib[fib.size()-2]);
    }
    while (t--) {
        cin >> n;
        tmp = n;
        ans = "";
        idx = upper_bound(fib.begin(), fib.end(), n) - fib.begin() - 1;
        for (int i = idx; i > 1; i--) {
            if (tmp >= fib[i]) {
                tmp -= fib[i];
                ans += "1";
            } else {
                ans += "0";
            }
        }
        cout << n << " = " << ans << " (fib)" << endl;
    }
    return 0;
}