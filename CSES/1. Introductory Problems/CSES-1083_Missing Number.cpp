#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x, ans;
    cin >> n;
    ans = n;
    for (int i = 1; i < n; i++) {
        cin >> x;
        ans ^= i ^ x;
    }
    cout << ans << endl;
    return 0;
}