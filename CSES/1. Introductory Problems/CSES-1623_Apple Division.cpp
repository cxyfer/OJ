#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<LL> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    LL s = 0;
    for (int i = 0; i < n; i++) s += nums[i];
    LL ans = s, s1, s2;
    for (int i = 1; i < (1 << n); i++) {
        s1 = 0;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                s1 += nums[j];
            }
        }
         s2 = s - s1;
        ans = min(ans, abs(s1 - s2));
    }
    cout << ans << endl;
    return 0;
}