#include <bits/stdc++.h>
using namespace std;
const int N = 105;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, tc=1, a, b;
    cin >> t;
    int pre_sum[N] = {0}; // prefix sum
    for (int i = 0; i <= 100; ++i) {
        pre_sum[i+1] = (i & 1) ? pre_sum[i] + i : pre_sum[i];
    }
    while (t--) {
        cin >> a >> b;
        cout << "Case " << tc++ << ": " << pre_sum[b+1] - pre_sum[a] << endl;
    }
    return 0;
}