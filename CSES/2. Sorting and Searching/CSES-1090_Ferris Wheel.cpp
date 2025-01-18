#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x; cin >> n >> x;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    sort(nums.begin(), nums.end());
    int ans = 0;
    int l = 0, r = n - 1;
    while (l <= r) {
        if (nums[l] + nums[r] <= x) l++;
        r--;
        ans++;
    }
    cout << ans << endl;
    return 0;
}