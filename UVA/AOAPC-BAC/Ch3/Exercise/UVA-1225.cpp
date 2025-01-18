#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, ans[10];
    cin >> t;
    while (t--) {
        cin >> n;
        memset(ans, 0, sizeof(ans));
        for (int x = 1; x <= n; x++) {
            int tmp = x;
            while (tmp) {
                ans[tmp % 10]++;
                tmp /= 10;
            }
        }
        for (int i = 0; i < 10; i++) {
            cout << ans[i];
            if (i != 9) cout << " ";
        }
        cout << endl;
    }
    return 0;
}