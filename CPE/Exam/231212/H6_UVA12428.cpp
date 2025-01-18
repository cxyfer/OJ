#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

void solve1() {
    LL n, m;
    cin >> n >> m;
    for (LL k = n-1; k >= 0; --k) {
        LL x = n - k;
        if (x * (x-1) / 2 >= m - k) {
            cout << k << endl;
            break;
        }
    }
}

void solve2() {
    LL n, m, x, k;
    cin >> n >> m;
    LL left = 0, right = n-1;
    while (left <= right) {
        k = (left + right) / 2; // mid
        x = n - k;
        if (x * (x-1) / 2 >= m - k) left = k + 1;
        else right = k - 1;
    }
    cout << right << endl;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL t, n, m;
    cin >> t;
    while (t--) {
        solve1();
        // solve2();
    }
    return 0;
}