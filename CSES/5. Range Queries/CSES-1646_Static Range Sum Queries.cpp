#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 2e5;
#define endl '\n'

LL nums[N], pre[N];
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, a, b;
    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        cin >> nums[i];
        pre[i] = pre[i - 1] + nums[i];
    }
    while (q--) {
        cin >> a >> b;
        cout << pre[b] - pre[a - 1] << endl;
    }
    return 0;
}