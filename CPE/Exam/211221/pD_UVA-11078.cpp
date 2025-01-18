#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, x;
    cin >> t;
    while (t--) {
        cin >> n;
        int mx, ans = INT_MIN;
        for (int i = 0; i < n; i++){
            if (i == 0) cin >> mx;
            else {
                cin >> x;
                ans = max(ans, mx - x);
                mx = max(mx, x);
            }
        }
        cout << ans << endl;
    }
    return 0;
}

// #include <bits/stdc++.h>
// using namespace std;
// const int N = 1e5 + 5;
// #define endl '\n'

// int main() {
//     ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
//     int t, n, A[N]; 
//     cin >> t;
//     while (t--) {
//         cin >> n;
//         for (int i = 0; i < n; i++) cin >> A[i];
//         int ans = INT_MIN, mx = A[0];
//         for (int i = 1; i < n; i++) {
//             ans = max(ans, mx - A[i]);
//             mx = max(mx, A[i]);
//         }
//         cout << ans << endl;
//     }
//     return 0;
// }