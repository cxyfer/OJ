#include <bits/stdc++.h>
using namespace std;

/*
決策單調性優化DP

Problems:
- 3826. Minimum Partition Score
- 3500. Minimum Cost to Divide Array Into Subarrays (Python TLE, C++ AC)
*/

class Solution {
public:
    long long minPartitionScore(vector<int>& nums, int k) {
        int n = nums.size();

        vector<long long> s(n + 1);
        for (int i = 0; i < n; i++) s[i + 1] = s[i] + nums[i];

        auto w = [&](int l, int r) -> long long {
            long long v = s[r] - s[l];
            return v * (v + 1) / 2;
        };

        vector<long long> f(n + 1, LLONG_MAX / 2), nf(n + 1, LLONG_MAX / 2);
        f[0] = 0;

        auto dfs = [&](this auto&& dfs, int l, int r, int opt_l,
                       int opt_r) -> void {
            if (l > r) return;
            int mid = l + (r - l) / 2;

            long long best_val = LLONG_MAX / 2;
            int opt = -1;
            for (int p = opt_l; p <= min(opt_r, mid - 1); p++) {
                long long v = f[p] + w(p, mid);
                if (v < best_val) {
                    best_val = v;
                    opt = p;
                }
            }

            nf[mid] = best_val;
            dfs(l, mid - 1, opt_l, opt);
            dfs(mid + 1, r, opt, opt_r);
            return;
        };

        for (int j = 1; j <= k; j++) {
            dfs(j, n, j - 1, n - 1);
            swap(f, nf);
        }
        return f[n];
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    Solution sol;
    vector<int> nums;
    int k;

    nums = {5,1,2,1};
    cout << sol.minPartitionScore(nums, 2) << endl;  // 25

    nums = {1,2,3,4};
    cout << sol.minPartitionScore(nums, 1) << endl;  // 55

    nums = {1,1,1};
    cout << sol.minPartitionScore(nums, 3) << endl;  // 3
    return 0;
}