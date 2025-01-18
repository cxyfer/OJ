#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL n; cin >> n;
    LL prev, curr, ans = 0;
    cin >> prev;
    for (int i = 1; i < n; i++) {
        cin >> curr;
        if (curr < prev) {
            ans += prev - curr;
        }
        else {
            prev = curr;
        }
    }
    cout << ans << endl;
    return 0;
}