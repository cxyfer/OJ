#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> A(n);
        for (int i = 0; i < n; ++i) cin >> A[i];

        int ans = 0, left = 0;
        unordered_map<int, int> cnt;
        for (int right = 0; right < n; right++) {
            cnt[A[right]]++;
            while (cnt[A[right]] > 1) {
                cnt[A[left]]--;
                left++;
            }
            ans = max(ans, right - left + 1);
        }
        cout << ans << endl;
    }
    return 0;
}