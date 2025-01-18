#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, N, I;
    double P, ans;
    cin >> t;
    while (t--) {
        cin >> N >> P >> I;
        if (P == 0) ans = 0;
        else ans = (pow(1 - P, I - 1) * P / (1 - pow(1 - P, N)));
        cout << fixed << setprecision(4) << ans << endl;
    }
    return 0;
}