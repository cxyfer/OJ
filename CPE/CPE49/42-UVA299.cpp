#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> arr(n);
        for (auto &x: arr) cin >> x;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                    ans++;
                }
            }
        }
        cout << "Optimal train swapping takes " << ans << " swaps." << endl;
    }
    return 0;
}