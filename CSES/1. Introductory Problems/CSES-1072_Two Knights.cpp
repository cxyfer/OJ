#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    for (int k = 1; k <= n; ++k)
        cout << (LL) (k * k - 1) * k * k / 2 - 4 * (k - 1) * (k - 2) << endl;
    return 0;
}