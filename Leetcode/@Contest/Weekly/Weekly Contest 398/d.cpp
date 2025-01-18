// class Solution:
//     """
//         Start at stair 1, then 
//         若當前 x > k+1，則永遠無法走到
//     """
//     def waysToReachStair(self, k: int) -> int:
//         @cache
//         def f(x, pre, can_down):
//             if x < 0: return 0
//             if x > k + 1: return 0 # 無法走到
//             res = 1 if x == k else 0
//             if can_down:
//                 res += f(x-1, pre, False) # 下1
//             res += f(x + 2**pre, pre+1, True)
//             return res
//         return f(1, 0, True)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int waysToReachStair(int k) {
        map<int, int> memo[32][2];
        function<int(int, int, bool)> f = [&](int x, int j, bool flag) -> int {
            if (x < 0) return 0;
            if (x > k + 1) return 0;
            if (memo[j][flag].count(x)) return memo[j][flag][x];
            int res = (x == k) ? 1 : 0;
            if (flag) res += f(x - 1, j, false);
            res += f(x + (1 << j), j + 1, true);
            return memo[j][flag][x] = res;
        };
        return f(1, 0, true);
    }
};