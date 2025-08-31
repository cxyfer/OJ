#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;
#define endl '\n'

#include <ranges>
class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        int mx = ranges::max(nums);
        int BITS = bit_width(static_cast<unsigned>(mx));

        vector<int> f(1 << BITS);
        for (int x : nums) f[x] = x;

        for (int i = 0; i < BITS; i++)
            for (int msk = 0; msk < (1 << BITS); msk++)
                if (msk >> i & 1) f[msk] = max(f[msk], f[msk ^ (1 << i)]);

        return ranges::max(nums | views::transform([&](int x) { return 1LL * x * f[((1 << BITS) - 1) ^ x]; }));
    }
};