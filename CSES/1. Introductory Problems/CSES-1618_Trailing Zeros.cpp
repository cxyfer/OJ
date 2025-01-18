#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    LL ans = 0;
    while (n >= 5) {
        ans += n / 5;
        n /= 5;
    }
    cout << ans << endl;
    return 0;
}