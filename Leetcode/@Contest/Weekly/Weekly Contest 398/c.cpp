
// class Solution:
//     def sumDigitDifferences(self, nums: List[int]) -> int:
//         cnt = defaultdict(Counter)
//         for x in nums:
//             d = 0
//             while x:
//                 cnt[d][x % 10] += 1
//                 x //= 10
//                 d += 1
//         # print(cnt)
//         ans = 0
//         for d in cnt:
//             tol = sum(cnt[d].values())
//             cur = 0
//             for k, v in cnt[d].items():
//                 cur += (tol - v) * v
//             ans += cur // 2
//             # print(d, ans)
//         return ans


#include <bits/stdc++.h>
using namespace std;

using LL = long long;
class Solution {
public:
    long long sumDigitDifferences(vector<int>& nums) {
        unordered_map<int, unordered_map<int, int>> cnt;
        for (int x : nums) {
            int d = 0;
            while (x) {
                cnt[d][x % 10]++;
                x /= 10;
                d++;
            }
        }
        LL ans = 0;
        for (auto p : cnt) {
            int d = p.first;
            LL tol = 0;
            for (auto kv : p.second) tol += kv.second;
            LL cur = 0;
            for (auto kv : p.second) {
                cur += (LL)(tol - kv.second) * kv.second;
            }
            ans += cur / 2;
        }
        return ans;
    }
};