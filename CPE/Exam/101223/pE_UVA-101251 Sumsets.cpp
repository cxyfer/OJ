#include <bits/stdc++.h>
using namespace std;
#define pii pair<int, int>
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    while (cin >> n && n) {
        vector<int> nums(n);
        for (int i = 0; i < n; i++) cin >> nums[i];
        unordered_map<int, vector<pii>> cnt;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                cnt[nums[i] + nums[j]].push_back({i, j});
            }
        }
        int ans = INT_MIN;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int target = nums[j] - nums[i];
                if (cnt.find(target) == cnt.end()) continue;
                for (auto &[i2, j2] : cnt[target]) {  
                    if (i != i2 && i != j2 && j != i2 && j != j2) {
                        ans = max(ans, nums[j]);
                    }
                }
            }
        }
        cout << (ans == INT_MIN ? "no solution" : to_string(ans)) << endl;
    }
    return 0;
}