#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 5;
#define endl '\n'

int nums[N];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    for (int i = 0; i < 3; i++) nums[i] = i + 1;
    for (int kase = 1; kase <= t; kase++) {
        int n, m, k;
        cin >> n >> m >> k;
        for (int i = 3; i < n; i++) nums[i] = (nums[i - 1] + nums[i - 2] + nums[i - 3]) % m + 1;
        int ans = n + 1, left = 0, have = 0;
        vector<int> cnt(k + 1);
        for (int right = 0; right < n; right++) {
            int x = nums[right];
            if (x > k) continue;
            if (cnt[x] == 0) have++;
            cnt[x]++;
            while (have == k) {
                ans = min(ans, right - left + 1);
                if (nums[left] <= k) {
                    cnt[nums[left]]--;
                    if (cnt[nums[left]] == 0) have--;
                }
                left++;
            }
        }
        cout << "Case " << kase << ": " << (ans == n + 1 ? "sequence nai" : to_string(ans)) << endl;
    }
    return 0;
}