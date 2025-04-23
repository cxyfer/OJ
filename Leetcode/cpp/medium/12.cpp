/*
 * @lc app=leetcode.cn id=12 lang=cpp
 * @lcpr version=30204
 *
 * [12] 整数转罗马数字
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
unordered_map<int, string> MP = {{1000, "M"}, {500, "D"}, {100, "C"}, {50, "L"}, {10, "X"}, {5, "V"}, {1, "I"}};
class Solution {
public:
    string intToRoman(int num) {
        string ans = "";
        int base = 1000;
        for (; num > 0; base /= 10) {
            int d = num / base;
            num %= base;
            if (d == 4) ans += MP[base] + MP[5 * base];
            else if (d == 9) ans += MP[base] + MP[10 * base];
            else {
                if (d > 4) {
                    ans += MP[5 * base];
                    d -= 5;
                }
                ans += string(d, MP[base][0]);
            }
        }
        return ans;
    }
};
// @lc code=end

// MP = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
// class Solution:
//     def intToRoman(self, num: int) -> str:
//         ans = ''
//         base = 1000
//         while num > 0:
//             d, num = divmod(num, base)
//             if d == 4:
//                 ans += MP[base] + MP[5 * base]
//             elif d == 9:
//                 ans += MP[base] + MP[10 * base]
//             else:
//                 if d > 4:
//                     ans += MP[5 * base]
//                     d -= 5
//                 ans += MP[base] * d
//             base //= 10
//         return ans

/*
// @lcpr case=start
// 3749\n
// @lcpr case=end

// @lcpr case=start
// 58\n
// @lcpr case=end

// @lcpr case=start
// 1994\n
// @lcpr case=end

 */

