#include <bits/stdc++.h>
using namespace std;
const int N = 30005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, nums[N];
    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> nums[i];
        }
        int ans = 1;
        int flag = 0; // 0: find smaller, 1: find larger
        for (int i = 1; i < n; i++) {
            if (flag == 0) {
                if (nums[i] < nums[i-1]) {
                    ans++;
                    flag ^= 1;
                }
            } else {
                if (nums[i] > nums[i-1]) {
                    ans++;
                    flag ^= 1;
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}